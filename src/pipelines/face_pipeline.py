import dlib
import face_recognition_models
import numpy as np
import streamlit as st

from src.database.db import get_all_students

RESEMBLANCE_THRESHOLD = 0.6


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(face_recognition_models.pose_predictor_model_location())

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec


def get_face_embeddings(image_np: np.ndarray) -> list[np.ndarray]:
    """Return face embeddings for an RGB uint8 image."""
    if (
        not isinstance(image_np, np.ndarray)
        or image_np.ndim != 3
        or image_np.shape[2] != 3
        or image_np.dtype != np.uint8
    ):
        raise ValueError("Expected an RGB uint8 image with three color channels.")

    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 1)

    encodings = []

    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(
            image_np, shape, 1
        )  # 128 embedding

        encodings.append(np.array(face_descriptor))
    return encodings


@st.cache_resource
def get_trained_model():
    X = []
    y = []

    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:
        embedding = student.get("face_embedding")
        student_id = student.get("student_id")
        if embedding is None or student_id is None:
            continue

        embedding = np.asarray(embedding, dtype=np.float64)
        if embedding.shape != (128,) or not np.isfinite(embedding).all():
            continue

        try:
            y.append(int(student_id))
        except (TypeError, ValueError) as exc:
            raise ValueError(
                f"Invalid student_id in student record: {student_id!r}"
            ) from exc
        X.append(embedding)

    if len(X) == 0:
        return None

    return {"X": np.stack(X), "y": np.asarray(y, dtype=np.int64)}


def train_classifier():
    get_trained_model.clear()
    model_data = get_trained_model()
    return bool(model_data)


def predict_attendance(class_image_np):
    """Return matched IDs with distance-based similarity scores, not probabilities."""
    encodings = get_face_embeddings(class_image_np)

    detected_student = {}

    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encodings)

    X_train = model_data["X"]
    y_train = model_data["y"]

    if len(X_train) == 0:
        return detected_student, [], len(encodings)

    all_students = sorted(set(y_train.tolist()))
    for encoding in encodings:
        distances = np.linalg.norm(X_train - encoding, axis=1)
        if len(distances) == 0:
            continue

        nearest_index = int(np.argmin(distances))
        best_match_distance = float(distances[nearest_index])
        if best_match_distance <= RESEMBLANCE_THRESHOLD:
            student_id = int(y_train[nearest_index])
            match_score = 1.0 - best_match_distance / RESEMBLANCE_THRESHOLD
            detected_student[student_id] = max(
                detected_student.get(student_id, 0.0),
                match_score,
            )

    return detected_student, all_students, len(encodings)
