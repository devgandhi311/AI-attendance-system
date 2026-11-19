from html import escape

import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div class="subject-card">
        <h3>{escape(str(name))}</h3>
        <p>Code: <span class="subject-code">{escape(str(code))}</span>
        &nbsp;·&nbsp; Section: {escape(str(section))}</p>
        """

    if stats:
        html += '<div class="subject-stats">'
        for icon, label, value in stats:
            html += (
                f'<div class="subject-stat">{escape(str(icon))} '
                f'<b>{escape(str(value))}</b> {escape(str(label))}</div>'
            )

        html += "</div>"

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
