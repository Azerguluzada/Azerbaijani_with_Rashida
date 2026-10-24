
from __future__ import annotations

import html
import re
from datetime import date
from pathlib import Path
from urllib.parse import quote

import streamlit as st
from config import BRAND

ROOT = Path(__file__).resolve().parent

st.set_page_config(
    page_title=BRAND.website_title,
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Brand colours and responsive design.
st.markdown(
    f"""
<style>
:root {{
 --purple:{BRAND.primary}; --deep:{BRAND.deep}; --yellow:{BRAND.yellow};
 --white:{BRAND.white}; --lavender:{BRAND.lavender}; --ink:{BRAND.ink};
 --muted:#6f687e; --line:#e9e2f5; --radius:24px;
}}
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
html {{scroll-behavior:smooth;}}
.stApp {{background:var(--white);color:var(--ink);font-family:'DM Sans',sans-serif;}}
header[data-testid="stHeader"] {{background:rgba(255,255,255,.92);}}
#MainMenu,footer,[data-testid="stToolbar"],[data-testid="stDecoration"] {{visibility:hidden;height:0;}}
.block-container {{max-width:1180px;padding:1rem 1.5rem 3rem;}}
section[data-testid="stSidebar"] {{display:none;}}
section.main > div {{padding-top:.5rem;}}
h1,h2,h3 {{font-family:'Manrope','DM Sans',sans-serif;letter-spacing:-.035em;color:var(--ink);}}
h1 {{font-size:clamp(2.6rem,5vw,4.6rem);line-height:1.04;font-weight:800;}}
h2 {{font-size:clamp(2rem,3.4vw,3rem);line-height:1.12;font-weight:800;}}
h3 {{font-size:1.2rem;font-weight:800;}}
p {{line-height:1.72;}}
a {{color:inherit;}}
.eyebrow {{display:inline-flex;gap:.5rem;align-items:center;font-size:.75rem;font-weight:800;letter-spacing:.13em;text-transform:uppercase;color:var(--purple);margin-bottom:.75rem;}}
.brandmark {{display:flex;align-items:center;gap:.65rem;font-family:'Manrope',sans-serif;font-weight:800;font-size:1.02rem;color:var(--deep);padding:.65rem 0 1.15rem;}}
.brand-icon {{width:38px;height:38px;border-radius:14px;display:grid;place-items:center;background:var(--yellow);font-size:1.2rem;}}
.navlinks {{display:flex;flex-wrap:wrap;align-items:center;justify-content:flex-end;gap:1.1rem;padding:.65rem 0 1.15rem;}}
.navlinks a {{text-decoration:none;font-size:.88rem;font-weight:700;color:#574c6e;}}
.navlinks a:hover {{color:var(--purple);}}
.pill-link {{display:inline-block;background:var(--purple);color:white!important;padding:.72rem 1.1rem;border-radius:999px;text-decoration:none!important;font-weight:800!important;}}
.hero {{background:radial-gradient(circle at 83% 20%,#835af0 0,transparent 30%),linear-gradient(130deg,var(--deep),#5126ad 65%,var(--purple));border-radius:32px;color:white;padding:clamp(2rem,5vw,4.6rem);position:relative;overflow:hidden;}}
.hero h1 {{color:white;max-width:720px;margin:.5rem 0 1.1rem;}}
.hero p {{color:#f2edff;max-width:610px;font-size:1.08rem;}}
.hero .eyebrow {{color:var(--yellow);}}
.hero-grid {{display:grid;grid-template-columns:1.25fr .75fr;gap:2rem;align-items:center;}}
.hero-art {{min-height:300px;display:flex;align-items:center;justify-content:center;position:relative;}}
.orbit {{width:260px;height:260px;border-radius:50%;background:linear-gradient(145deg,#f5edff,#d6c4ff);display:grid;place-items:center;box-shadow:inset 0 0 0 14px #ffffff40;position:relative;transform:rotate(4deg);}}
.pet {{font-size:8rem;filter:drop-shadow(0 12px 8px #32145f24);transform:rotate(-5deg);}}
.bubble {{position:absolute;background:var(--yellow);color:var(--deep);padding:.7rem 1rem;border-radius:18px 18px 18px 5px;font-weight:800;box-shadow:0 8px 24px #1b083e33;}}
.bubble.one {{top:10px;right:-4px;transform:rotate(5deg);}}
.bubble.two {{left:-18px;bottom:30px;background:white;transform:rotate(-5deg);}}
.hero-cta {{display:flex;gap:.8rem;flex-wrap:wrap;margin-top:1.6rem;}}
.cta-primary,.cta-secondary {{display:inline-block;padding:.9rem 1.25rem;border-radius:999px;text-decoration:none;font-weight:800;transition:transform .18s,box-shadow .18s;}}
.cta-primary {{background:var(--yellow);color:var(--deep);box-shadow:0 7px 0 #e9b92e;}}
.cta-secondary {{border:1px solid #ffffff70;color:white;background:#ffffff12;}}
.cta-primary:hover,.cta-secondary:hover {{transform:translateY(-2px);}}
.section {{padding:5rem 0 .5rem;scroll-margin-top:24px;}}
.section-intro {{max-width:690px;margin-bottom:2rem;}}
.section-intro p {{color:var(--muted);font-size:1.05rem;}}
.card {{height:100%;padding:1.5rem;background:white;border:1px solid var(--line);border-radius:var(--radius);box-shadow:0 10px 32px #32145f08;transition:transform .2s,box-shadow .2s;}}
.card:hover {{transform:translateY(-4px);box-shadow:0 18px 38px #32145f12;}}
.card-icon {{width:52px;height:52px;display:grid;place-items:center;border-radius:17px;background:var(--lavender);font-size:1.55rem;margin-bottom:1.1rem;}}
.card p {{color:var(--muted);margin-bottom:.4rem;}}
.lesson-card {{background:linear-gradient(180deg,#fff 0%,#fcfaff 100%);}}
.mini-lesson {{background:var(--lavender);border-radius:28px;padding:clamp(1.4rem,3vw,2.4rem);}}
.phrase {{background:white;border:1px solid #e6dcfb;border-radius:16px;padding:1rem 1.1rem;margin-bottom:.7rem;display:flex;justify-content:space-between;gap:1rem;align-items:center;}}
.phrase strong {{color:var(--deep);font-size:1.06rem;}}
.phrase span {{color:var(--muted);text-align:right;}}
.about-panel {{background:#fbf9ff;border-radius:28px;padding:clamp(1.5rem,4vw,3rem);border:1px solid var(--line);}}
.portrait-placeholder {{min-height:340px;height:100%;border-radius:24px;background:linear-gradient(145deg,#e6dbff,#fff0a8);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:1.5rem;color:var(--deep);}}
.portrait-placeholder .portrait-emoji {{font-size:5rem;margin-bottom:.7rem;}}
.culture-card {{background:#fffdf5;border-color:#f5edce;}}
.footer {{border-top:1px solid var(--line);margin-top:4rem;padding:2rem 0 1rem;color:var(--muted);font-size:.9rem;}}
.small-muted {{color:var(--muted);font-size:.85rem;}}
.final-cta {{background:linear-gradient(125deg,var(--deep),var(--purple));border-radius:30px;padding:clamp(2rem,5vw,4rem);text-align:center;color:white;margin-top:5rem;}}
.final-cta h2 {{color:white;max-width:760px;margin:0 auto 1rem;}}
.final-cta p {{color:#eee7ff;max-width:650px;margin:0 auto 1.5rem;}}
div[data-testid="stButton"] > button,div[data-testid="stFormSubmitButton"] > button {{border-radius:999px;border:0;background:var(--purple);color:white;font-weight:800;min-height:2.8rem;padding:.45rem 1.15rem;}}
div[data-testid="stButton"] > button:hover,div[data-testid="stFormSubmitButton"] > button:hover {{background:var(--deep);color:white;}}
div[data-testid="stAlert"] {{border-radius:14px;}}
@media(max-width:760px) {{
 .block-container {{padding-left:1rem;padding-right:1rem;}}
 .hero-grid {{grid-template-columns:1fr;}}
 .hero-art {{min-height:245px;}}
 .orbit {{width:210px;height:210px;}}
 .pet {{font-size:6.5rem;}}
 .bubble.one {{right:4px;}}
 .bubble.two {{left:0;}}
 .section {{padding-top:3.5rem;}}
 .navlinks {{justify-content:flex-start;gap:.8rem;padding-top:0;}}
 .brandmark {{padding-bottom:.5rem;}}
 .phrase {{align-items:flex-start;flex-direction:column;gap:.2rem;}}
 .phrase span {{text-align:left;}}
}}
</style>
""",
    unsafe_allow_html=True,
)


def section_heading(kicker: str, title: str, description: str) -> None:
    st.markdown(
        f'<div class="section-intro"><div class="eyebrow">{html.escape(kicker)}</div>'
        f'<h2>{html.escape(title)}</h2><p>{html.escape(description)}</p></div>',
        unsafe_allow_html=True,
    )


def card(icon: str, title: str, description: str, extra_class: str = "") -> None:
    st.markdown(
        f'<div class="card {extra_class}"><div class="card-icon">{icon}</div>'
        f'<h3>{html.escape(title)}</h3><p>{html.escape(description)}</p></div>',
        unsafe_allow_html=True,
    )


def instagram_is_configured() -> bool:
    return "REPLACE_WITH_INSTAGRAM_HANDLE" not in BRAND.instagram_url


def email_is_configured() -> bool:
    return "REPLACE_WITH_CONTACT_EMAIL" not in BRAND.contact_email


def contact_links() -> None:
    cols = st.columns([1, 1, 2])
    if instagram_is_configured():
        cols[0].link_button(
            "Instagram DM ↗", BRAND.instagram_url, use_container_width=True
        )
    else:
        cols[0].button(
            "Instagram DM ↗", disabled=True, use_container_width=True,
            help="Add the real Instagram URL in config.py",
        )
    if email_is_configured():
        cols[1].link_button(
            "Email Rashida ↗",
            f"mailto:{BRAND.contact_email}",
            use_container_width=True,
        )
    else:
        cols[1].button(
            "Email Rashida ↗", disabled=True, use_container_width=True,
            help="Add the real email address in config.py",
        )
    cols[2].markdown(
        '<div class="small-muted" style="padding:.6rem 0">'
        'Replace the contact placeholders in <code>config.py</code> before publishing.'
        '</div>',
        unsafe_allow_html=True,
    )


# Navigation
nav_left, nav_right = st.columns([1.05, 2.2], vertical_alignment="center")
with nav_left:
    st.markdown(
        '<div class="brandmark"><span class="brand-icon">💬</span>'
        '<span>Azerbaijani<br>with Rashida</span></div>',
        unsafe_allow_html=True,
    )
with nav_right:
    st.markdown(
        """<div class="navlinks">
        <a href="#home">Home</a>
        <a href="#lessons">Lessons</a>
        <a href="#about">About Rashida</a>
        <a href="#culture">Culture</a>
        <a href="#faq">FAQ</a>
        <a class="pill-link" href="#contact">Start Learning ↗</a>
        </div>""",
        unsafe_allow_html=True,
    )

# Hero
st.markdown(
    """
<div id="home" class="hero">
  <div class="hero-grid">
    <div>
      <div class="eyebrow">✦ Your journey into Azerbaijani starts here</div>
      <h1>Speak Azerbaijani.<br>Connect with Azerbaijan.</h1>
      <p>Learn the language, discover the culture, and feel more confident in
      real-life conversations. Practical Azerbaijani lessons designed to help
      you speak naturally.</p>
      <div class="hero-cta">
        <a class="cta-primary" href="#lessons">Explore Lessons ↗</a>
        <a class="cta-secondary" href="#about">Meet Rashida</a>
      </div>
    </div>
    <div class="hero-art" aria-label="Playful language-learning illustration">
      <div class="orbit">
        <div class="pet" role="img" aria-label="Friendly cartoon cat">🐱</div>
        <div class="bubble one">Salam! 👋</div>
        <div class="bubble two">Çox sağ ol!</div>
      </div>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# Benefits
st.markdown('<div class="section" id="why">', unsafe_allow_html=True)
section_heading(
    "A better way to learn",
    "More Than Just Words",
    "Learn Azerbaijani the way people actually speak it.",
)
a, b, c = st.columns(3, gap="large")
with a:
    card("💬", "Speak Naturally",
         "Learn practical expressions and everyday conversations you can use in real life.")
with b:
    card("🧿", "Discover the Culture",
         "Understand the traditions, expressions, and social customs that make communication meaningful.")
with c:
    card("🌱", "Learn With Confidence",
         "Build your vocabulary, improve your pronunciation, and feel more comfortable speaking Azerbaijani.")
st.markdown("</div>", unsafe_allow_html=True)

# Lessons
st.markdown('<div class="section" id="lessons">', unsafe_allow_html=True)
section_heading(
    "Lessons for real life",
    "Find Your Way to Azerbaijani",
    "Whether you're starting from zero or looking to improve your everyday "
    "conversations, let's find the right approach for you.",
)
lesson_cols = st.columns(3, gap="large")
lesson_data = [
    ("🌼", "Azerbaijani for Beginners",
     "Start with greetings, introductions, useful vocabulary, and the foundations of everyday conversation."),
    ("🗣️", "Everyday Azerbaijani",
     "Learn useful expressions, natural replies, and the phrases you need to communicate with local people."),
    ("🌍", "Language & Culture",
     "Explore Azerbaijani idioms, traditions, cultural expressions, and the language people use in everyday life."),
]
for col, item in zip(lesson_cols, lesson_data):
    with col:
        card(*item, extra_class="lesson-card")
        st.markdown('<div style="height:.8rem"></div>', unsafe_allow_html=True)
        if instagram_is_configured():
            st.link_button(
                "Ask About Lessons ↗", BRAND.instagram_url,
                use_container_width=True,
            )
        else:
            st.button(
                "Ask About Lessons", key=f"lesson_{item[1]}",
                disabled=True, use_container_width=True,
                help="Add Rashida's Instagram URL in config.py",
            )
st.markdown("</div>", unsafe_allow_html=True)

# About Rashida
st.markdown('<div class="section" id="about">', unsafe_allow_html=True)
section_heading(
    "A little introduction",
    "Meet Your Azerbaijani Teacher",
    "A friendly, practical approach to language and culture.",
)
about_l, about_r = st.columns(
    [1, 1.35], gap="large", vertical_alignment="center"
)
with about_l:
    portrait = ROOT / BRAND.portrait_path
    if portrait.is_file():
        st.image(str(portrait), caption="Rashida", use_container_width=True)
    else:
        st.markdown(
            '<div class="portrait-placeholder">'
            '<div class="portrait-emoji">🌷</div>'
            '<h3>Your portrait goes here</h3>'
            '<p>Add a real photo at<br>'
            '<code>assets/images/rashida-portrait.jpg</code></p></div>',
            unsafe_allow_html=True,
        )
with about_r:
    st.markdown(
        """<div class="about-panel">
        <div class="eyebrow">Salam! 👋</div>
        <h3 style="font-size:1.65rem">I'm Rashida.</h3>
        <p>I'm passionate about helping people discover Azerbaijani through
        practical language learning, everyday conversations, and cultural
        understanding.</p>
        <p>My goal is to help you feel more confident using Azerbaijani in
        real-life situations — from your first greetings to the expressions
        that make conversations feel more natural.</p>
        <p>Learning a language is not just about grammar. It's about connecting
        with people, understanding their culture, and feeling at home in a
        conversation.</p>
        <p><strong>Let's make Azerbaijani part of your everyday life!</strong></p>
        </div>""",
        unsafe_allow_html=True,
    )
    st.markdown('<div style="height:.8rem"></div>', unsafe_allow_html=True)
    st.markdown(
        '<a class="cta-primary" href="#contact">Let’s Start Learning ↗</a>',
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)

# Azerbaijani culture
st.markdown('<div class="section" id="culture">', unsafe_allow_html=True)
section_heading(
    "More than vocabulary",
    "Discover Azerbaijan Beyond the Textbook",
    "Language makes more sense when you understand the culture behind it.",
)
culture_cols = st.columns(3, gap="large")
culture_data = [
    ("🍵", "Azerbaijani Hospitality",
     "Welcoming guests and offering tea or food are important parts of hospitality in many Azerbaijani households."),
    ("✨", "Everyday Expressions",
     "Explore useful Azerbaijani phrases and what they mean in natural, everyday conversation."),
    ("🤝", "Unwritten Cultural Rules",
     "Discover common customs and social habits that can help visitors better understand local life."),
]
for col, item in zip(culture_cols, culture_data):
    with col:
        card(*item, extra_class="culture-card")
        st.markdown('<div style="height:.8rem"></div>', unsafe_allow_html=True)
        st.markdown(
            '<a class="pill-link" href="#mini-lesson">Explore More ↗</a>',
            unsafe_allow_html=True,
        )
st.markdown("</div>", unsafe_allow_html=True)

# Mini lesson and quiz
st.markdown('<div class="section" id="mini-lesson">', unsafe_allow_html=True)
section_heading(
    "A tiny first lesson",
    "Learn Your First Azerbaijani Phrases",
    "Start with expressions you can use right away. Reveal the meanings, "
    "then try a quick quiz.",
)
left, right = st.columns([1.05, .95], gap="large")
phrases = [
    ("Salam!", "Hello!"),
    ("Necəsən?", "How are you?"),
    ("Çox sağ ol!", "Thank you!"),
    ("Nuş olsun!", "Enjoy your meal!"),
    ("Sonra görüşərik!", "See you later!"),
]
with left:
    st.markdown('<div class="mini-lesson">', unsafe_allow_html=True)
    if "show_phrase_meanings" not in st.session_state:
        st.session_state.show_phrase_meanings = False
    for az, en in phrases:
        meaning = (
            en if st.session_state.show_phrase_meanings
            else "Tap Reveal Meaning to see the translation"
        )
        st.markdown(
            f'<div class="phrase"><strong>{html.escape(az)}</strong>'
            f'<span>{html.escape(meaning)}</span></div>',
            unsafe_allow_html=True,
        )
    if st.button(
        "Hide Meanings" if st.session_state.show_phrase_meanings
        else "Reveal Meaning",
        key="reveal_meanings",
        use_container_width=True,
    ):
        st.session_state.show_phrase_meanings = (
            not st.session_state.show_phrase_meanings
        )
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown(
        '<div class="card"><div class="eyebrow">✦ Quick practice</div>'
        '<h3>Check what you remember</h3>'
        '<p>Choose the best English meaning for each phrase.</p></div>',
        unsafe_allow_html=True,
    )
    with st.form("phrase_quiz"):
        q1 = st.radio(
            "1. What does ‘Salam!’ mean?",
            ["Goodbye!", "Hello!", "Good night!"],
            index=None, key="quiz_q1",
        )
        q2 = st.radio(
            "2. What does ‘Çox sağ ol!’ mean?",
            ["Thank you!", "How are you?", "Enjoy your meal!"],
            index=None, key="quiz_q2",
        )
        q3 = st.radio(
            "3. What does ‘Nuş olsun!’ mean?",
            ["See you later!", "Hello!", "Enjoy your meal!"],
            index=None, key="quiz_q3",
        )
        submitted = st.form_submit_button("Check My Answers")
    if submitted:
        answers = [q1, q2, q3]
        if any(answer is None for answer in answers):
            st.warning("Please answer all three questions before checking your score.")
        else:
            score = sum([
                q1 == "Hello!",
                q2 == "Thank you!",
                q3 == "Enjoy your meal!",
            ])
            st.session_state.quiz_score = score
            st.session_state.quiz_submitted = True
    if st.session_state.get("quiz_submitted", False):
        st.success(f"Your score: {st.session_state.quiz_score}/3")
        st.markdown(
            "**Correct answers:** Salam! = Hello · "
            "Çox sağ ol! = Thank you · Nuş olsun! = Enjoy your meal"
        )
st.markdown("</div>", unsafe_allow_html=True)

# Contact section
st.markdown('<div class="section" id="contact">', unsafe_allow_html=True)
section_heading(
    "Your next step",
    "Ready to Start Speaking Azerbaijani?",
    "Tell me a little about your goals, and let's find the right way for you to start learning.",
)
contact_links()

st.markdown('<div style="height:1rem"></div>', unsafe_allow_html=True)
with st.expander("Prefer to write a message here? (Optional contact form)"):
    st.info(
        "This starter project does not send or store form submissions. "
        "Until a messaging service is configured, use the Instagram or email "
        "buttons above. No false delivery confirmation will be shown."
    )
    with st.form("contact_form", clear_on_submit=False):
        name = st.text_input("Name *", max_chars=100)
        email = st.text_input("Email address *", max_chars=254)
        goals = st.selectbox(
            "What would you like to learn? *",
            [
                "Choose a goal…",
                "I'm a complete beginner",
                "Everyday conversation",
                "Azerbaijani for travel",
                "Language and culture",
                "Something else",
            ],
        )
        message = st.text_area(
            "Optional message", max_chars=2000,
            placeholder="Tell Rashida a little about your goals…",
        )
        form_submit = st.form_submit_button("Prepare Email")

    if form_submit:
        if not name.strip() or not email.strip() or goals == "Choose a goal…":
            st.error("Please complete your name, email address, and learning goal.")
        elif not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email.strip()):
            st.error("Please enter a valid email address.")
        elif not email_is_configured():
            st.warning(
                "The contact email is still a placeholder. "
                "Update config.py before using this form."
            )
        else:
            subject = quote(
                f"Azerbaijani lesson enquiry from {name.strip()}"
            )
            body = quote(
                f"Name: {name.strip()}\n"
                f"Email: {email.strip()}\n"
                f"Learning goal: {goals}\n\n"
                f"Message:\n{message.strip()}"
            )
            st.markdown(
                f"[Open your email app to send this enquiry]"
                f"(mailto:{BRAND.contact_email}?subject={subject}&body={body})"
            )
            st.caption(
                "Your email app will open with a draft. You still need to press "
                "Send; this website does not transmit the message."
            )
st.markdown("</div>", unsafe_allow_html=True)

# FAQ
st.markdown('<div class="section" id="faq">', unsafe_allow_html=True)
section_heading(
    "Good to know",
    "Frequently Asked Questions",
    "A few helpful details before you get started.",
)
faqs = [
    (
        "Can I start learning Azerbaijani with no previous experience?",
        "Absolutely! The beginner lessons are designed for people who are starting from zero.",
    ),
    (
        "Are the lessons focused on speaking or grammar?",
        "The focus is on practical communication, everyday expressions, and cultural "
        "understanding, with grammar introduced when it helps you communicate more naturally.",
    ),
    (
        "Do I need to know Russian or Turkish?",
        "No. You can begin learning Azerbaijani without knowing either language.",
    ),
    (
        "Are the lessons online?",
        "Contact Rashida to discuss lesson arrangements and availability.",
    ),
    (
        "How can I find out about prices and availability?",
        "Send Rashida a message to discuss your learning goals, lesson options, "
        "and current availability.",
    ),
]
for question, answer in faqs:
    with st.expander(question):
        st.write(answer)
st.markdown("</div>", unsafe_allow_html=True)

# Final call to action
st.markdown(
    """<div class="final-cta">
    <div class="eyebrow" style="color:#ffd84d">✦ Your next chapter</div>
    <h2>Your First Azerbaijani Conversation Starts Here.</h2>
    <p>Take the first step toward speaking naturally and connecting with Azerbaijani culture.</p>
    <a class="cta-primary" href="#contact">Message Rashida ↗</a>
    </div>""",
    unsafe_allow_html=True,
)

# Footer
st.markdown('<div class="footer">', unsafe_allow_html=True)
foot_l, foot_r = st.columns([1, 1], vertical_alignment="center")
with foot_l:
    st.markdown(
        "**Azerbaijani with Rashida**  \n"
        "Speak naturally. Connect with Azerbaijan."
    )
with foot_r:
    st.markdown(
        '<div style="text-align:right">'
        '<a href="#home">Home</a> · '
        '<a href="#lessons">Lessons</a> · '
        '<a href="#about">About</a> · '
        '<a href="#culture">Culture</a> · '
        '<a href="#faq">FAQ</a></div>',
        unsafe_allow_html=True,
    )
st.markdown(
    f'<p class="small-muted">© {date.today().year} Azerbaijani with Rashida. '
    "Configure contact details and any legally required business information "
    "before public launch.</p>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)
