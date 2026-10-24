"""
Azerbaijani with Rashida: single-page website built with Streamlit.

Run locally:   streamlit run app.py
Edit details:  config.py (contact, images, colours)  and  content.py (text)
"""

from __future__ import annotations

import logging
import time
from html import escape

import streamlit as st

import components as ui
import config
import contact
import content
import quiz
import styles

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Page setup (must be the first Streamlit call)
# ---------------------------------------------------------------------------
def _page_icon() -> str:
    candidate = config.BASE_DIR / config.PAGE_ICON
    return str(candidate) if candidate.is_file() else config.PAGE_ICON


st.set_page_config(
    page_title=config.PAGE_TITLE,
    page_icon=_page_icon(),
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"About": f"{config.BRAND_NAME}. {config.META_DESCRIPTION}"},
)


def inject_css() -> None:
    st.html(f"<style>{styles.build_css()}</style>")


# ---------------------------------------------------------------------------
# Session state (used only for the phrase reveal and the quiz)
# ---------------------------------------------------------------------------
def init_state() -> None:
    st.session_state.setdefault("show_meanings", False)
    st.session_state.setdefault("quiz_round", 0)  # bumping this resets the quiz widgets
    st.session_state.setdefault("quiz_result", None)
    st.session_state.setdefault("last_send_ts", 0.0)


def _toggle_meanings() -> None:
    st.session_state.show_meanings = not st.session_state.show_meanings


def _reset_quiz() -> None:
    st.session_state.quiz_round += 1
    st.session_state.quiz_result = None


# ---------------------------------------------------------------------------
# Sections
# ---------------------------------------------------------------------------
def render_setup_banner() -> None:
    problems = config.setup_problems()
    if config.SHOW_SETUP_WARNINGS and problems:
        with st.container(key="setup-banner"):
            st.warning(
                "**Setup reminder (only you see this while placeholders remain):** "
                "please update " + ", ".join(problems) + " in `config.py` before going public. "
                "Set `SHOW_SETUP_WARNINGS = False` to hide this message.",
                icon="🛠️",
            )


def render_quiz() -> None:
    ss = st.session_state
    qz = content.QUIZ_INTRO
    round_id = ss.quiz_round

    with st.container(key="quiz-card"):
        st.html(f'<h3 class="card-heading">{escape(qz["heading"])}</h3><p class="card-sub">{escape(qz["text"])}</p>')

        if ss.quiz_result is None:
            with st.form(f"quiz_form_{round_id}", border=False):
                for i, q in enumerate(content.QUIZ):
                    st.radio(q["question"], q["options"], index=None, key=f"quiz_{round_id}_{i}")
                submitted = st.form_submit_button(qz["submit"])

            if submitted:
                answers = [ss.get(f"quiz_{round_id}_{i}") for i in range(len(content.QUIZ))]
                if any(a is None for a in answers):
                    st.warning(qz["incomplete"])
                else:
                    ss.quiz_result = quiz.grade_quiz(answers)
                    st.rerun()
        else:
            result = ss.quiz_result
            rows = []
            for r in result["results"]:
                css, tag = ("ok", "✓ Correct") if r["is_correct"] else ("no", "✗ Not quite")
                your = "" if r["is_correct"] else f'<p class="a">Your answer: {escape(str(r["chosen"]))}</p>'
                rows.append(
                    f'<div class="result {css}"><span class="tag">{tag}</span>'
                    f'<p class="q">{escape(r["question"])}</p>{your}'
                    f'<p class="a"><strong>Correct answer:</strong> <span lang="az">{escape(r["correct_answer"])}</span></p>'
                    f'<p class="why">{escape(r["explanation"])}</p></div>'
                )
            st.html(
                '<div class="score-banner" role="status">'
                f'<span class="score-num">{result["score"]} / {result["total"]}</span>'
                f'<span class="score-msg">{escape(quiz.score_message(result["score"], result["total"]))}</span></div>'
                + "".join(rows)
            )
            st.button(qz["retry"], key="quiz_retry", on_click=_reset_quiz)


def render_phrases() -> None:
    ss = st.session_state
    data = content.PHRASES_SECTION
    with st.container(key="sec-phrases"):
        st.html(ui.phrases_head_html())
        with st.container(key="reveal-row"):
            st.button(
                data["hide_button"] if ss.show_meanings else data["reveal_button"],
                key="toggle_meanings",
                on_click=_toggle_meanings,
            )
        st.html(ui.phrase_grid_html(ss.show_meanings))
        render_quiz()


def _show_contact_fallbacks(name: str, email: str, goals: str, message: str) -> None:
    """Honest fallbacks: pre-filled email and Instagram. Nothing has been sent."""
    if config.email_configured():
        mailto = contact.build_mailto(
            config.CONTACT_EMAIL,
            config.CONTACT_FORM["email_subject"],
            contact.build_body(name, email, goals, message),
        )
        st.link_button(content.CONTACT["prefilled_email_button"], mailto, icon=":material/mail:")
    else:
        st.warning("Rashida's email address has not been set up yet (`CONTACT_EMAIL` in `config.py`).")
    if config.instagram_configured():
        st.link_button(content.CONTACT["instagram_button"], config.INSTAGRAM_URL, icon=":material/chat:")


def handle_contact_submit(name: str, email: str, goals: str, message: str) -> None:
    text = content.CONTACT
    errors = contact.validate_form(name, email, goals, message)
    if errors:
        for field_error in errors.values():
            st.error(field_error)
        return

    settings = contact.load_smtp_settings()
    if settings is None:
        # No e-mail service configured: be honest, never show a success message.
        st.info(text["not_configured"])
        _show_contact_fallbacks(name, email, goals, message)
        return

    cooldown = config.CONTACT_FORM["cooldown_seconds"]
    if time.time() - st.session_state.last_send_ts < cooldown:
        st.warning(text["cooldown"])
        return

    try:
        contact.send_email(settings, name, email, goals, message)
    except Exception as exc:  # network, login, or SMTP errors
        # Log only the error type, never visitor data or credentials.
        logger.warning("Contact email could not be sent (%s).", type(exc).__name__)
        st.error(text["send_failed"])
        _show_contact_fallbacks(name, email, goals, message)
    else:
        st.session_state.last_send_ts = time.time()
        st.success(text["send_ok"])


def render_contact() -> None:
    text = content.CONTACT
    limits = config.CONTACT_FORM
    with st.container(key="sec-contact"):
        st.html(ui.contact_head_html())

        if not limits["enabled"]:
            return

        with st.container(key="contact-card"):
            st.html(f'<h3 class="card-heading">{escape(text["form_heading"])}</h3>')
            with st.form("contact_form", border=False):
                name = st.text_input(text["name_label"], max_chars=limits["max_name"], key="cf_name")
                email = st.text_input(text["email_label"], max_chars=limits["max_email"], key="cf_email")
                goals = st.text_area(
                    text["goals_label"], help=text["goals_help"], max_chars=limits["max_goals"], height=110, key="cf_goals"
                )
                message = st.text_area(text["message_label"], max_chars=limits["max_message"], height=110, key="cf_message")
                submitted = st.form_submit_button(text["submit"])
            st.caption(text["privacy_hint"])
            if submitted:
                handle_contact_submit(name, email, goals, message)


def render_faq() -> None:
    with st.container(key="sec-faq"):
        st.html(ui.faq_head_html())
        for question, answer in content.FAQ["items"]:
            with st.expander(question):
                st.write(answer)


def render_footer() -> None:
    with st.container(key="sec-footer"):
        st.html(ui.footer_html())
        with st.expander(content.PRIVACY_TITLE):
            st.markdown(content.PRIVACY_TEXT)


# ---------------------------------------------------------------------------
# Page
# ---------------------------------------------------------------------------
def main() -> None:
    init_state()
    inject_css()
    st.html(ui.nav_html())

    with st.container(key="sec-hero"):
        st.html(ui.hero_html())
    render_setup_banner()

    with st.container(key="sec-why"):
        st.html(ui.why_html())
    with st.container(key="sec-lessons"):
        st.html(ui.lessons_html())
    with st.container(key="sec-about"):
        st.html(ui.about_html())
    with st.container(key="sec-culture"):
        st.html(ui.culture_html())

    render_phrases()
    render_contact()
    render_faq()

    with st.container(key="sec-cta"):
        st.html(ui.final_cta_html())

    render_footer()


main()
