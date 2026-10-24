"""
Central configuration for "Azerbaijani with Rashida".

Everything a non-developer may want to change lives in THIS file:
contact details, page title, colours, optional images, and feature switches.

Values containing the text "REPLACE_WITH" are placeholders. Replace them
before the website goes public. While placeholders remain, the app shows a
yellow setup warning (see SHOW_SETUP_WARNINGS below).

NEVER put passwords or API keys in this file. Secrets belong in
.streamlit/secrets.toml (local) or the Streamlit Community Cloud
"Secrets" settings. See README.md, section 13.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# 1. Brand and page metadata
# ---------------------------------------------------------------------------
BRAND_NAME = "Azerbaijani with Rashida"
TEACHER_NAME = "Rashida"
TAGLINE = "Speak naturally. Connect with Azerbaijan."

PAGE_TITLE = "Azerbaijani with Rashida | Learn Azerbaijani Online"
META_DESCRIPTION = (
    "Learn Azerbaijani with Rashida through practical conversations, "
    "everyday expressions, and cultural insights."
)
PAGE_ICON = "💬"  # An emoji, or a path to a small image such as "assets/images/favicon.png"

# ---------------------------------------------------------------------------
# 2. Contact details  (PLACEHOLDERS: replace before launch)
# ---------------------------------------------------------------------------
# Full link to Rashida's Instagram profile, e.g. "https://www.instagram.com/her_handle/"
INSTAGRAM_URL = "https://www.instagram.com/REPLACE_WITH_INSTAGRAM_HANDLE/"
# How the handle is displayed on the page, e.g. "@her_handle"
INSTAGRAM_LABEL = "@REPLACE_WITH_INSTAGRAM_HANDLE"

# Public contact e-mail shown on the website (used for the mailto: button).
CONTACT_EMAIL = "REPLACE_WITH_CONTACT_EMAIL"

# ---------------------------------------------------------------------------
# 3. Optional images (all paths are relative to this folder)
# ---------------------------------------------------------------------------
# Portrait of Rashida. Put a real photo at this path (jpg/png/webp, ideally
# under 500 KB, roughly square or 4:5). If the file does not exist, a friendly
# "photo coming soon" placeholder is shown instead.
PORTRAIT_PATH = "assets/images/rashida.jpg"
PORTRAIT_ALT = "Portrait of Rashida, your Azerbaijani teacher"

# Optional approved brand illustration (for example the Instagram cat or dog)
# to use in the hero instead of the built-in cartoon cat. Leave "" to keep the
# built-in cat. Only use artwork you have the right to publish.
HERO_IMAGE_PATH = ""
HERO_IMAGE_ALT = "Friendly cartoon character saying hello in Azerbaijani"

# Optional logo image. Leave "" to use the built-in typographic wordmark.
LOGO_PATH = ""

# ---------------------------------------------------------------------------
# 4. Brand colours  (turned into CSS variables, see styles.py)
# ---------------------------------------------------------------------------
COLORS = {
    "purple": "#6C3CE9",       # primary purple
    "purple_deep": "#32145F",  # deep purple
    "yellow": "#FFD84D",       # bright yellow
    "white": "#FFFFFF",
    "lavender": "#F3EEFF",     # soft lavender
    "ink": "#211936",          # dark text
    "muted": "#5B5170",        # secondary text (checked for contrast on white and lavender)
}

# Load the Inter font from Google Fonts. Set to False to use only system fonts
# (e.g. if you prefer not to contact Google servers; see README, "Privacy").
USE_GOOGLE_FONTS = True

# ---------------------------------------------------------------------------
# 5. Lesson buttons and (future) pricing
# ---------------------------------------------------------------------------
# What the "Ask About Lessons" buttons do: "contact" scrolls to the contact
# section, "instagram" opens the Instagram profile in a new tab.
LESSON_BUTTON_ACTION = "contact"

# Prices are intentionally NOT invented. To show a price on a lesson card
# later, add an entry here using the lesson id from content.py, e.g.
#   LESSON_PRICES = {"beginners": "From 25 EUR / lesson"}
# Lessons without an entry show no price at all.
LESSON_PRICES: dict[str, str] = {}

# ---------------------------------------------------------------------------
# 6. Contact form
# ---------------------------------------------------------------------------
CONTACT_FORM = {
    # Show the form at all. The Instagram and e-mail buttons always stay visible.
    "enabled": True,
    # Subject line used for e-mails created by the form.
    "email_subject": "New Azerbaijani lesson enquiry",
    # Minimum seconds between two e-mails sent from the same browser session.
    "cooldown_seconds": 60,
    # Field limits (characters).
    "max_name": 100,
    "max_email": 254,
    "max_goals": 1000,
    "max_message": 2000,
}

# ---------------------------------------------------------------------------
# 7. Legal / privacy  (keep configurable; do NOT invent details)
# ---------------------------------------------------------------------------
# Business or legal details required in your country (company name, address,
# registration or VAT number, "Impressum" ...). Leave "" until you have them.
# Plain text; blank lines separate paragraphs. Shown in the footer if not empty.
LEGAL_NOTICE = ""

# ---------------------------------------------------------------------------
# 8. Development helpers
# ---------------------------------------------------------------------------
# Show a visible warning on the page while placeholders above are unchanged.
SHOW_SETUP_WARNINGS = True


# ---------------------------------------------------------------------------
# Helpers (no need to edit below this line)
# ---------------------------------------------------------------------------
def is_placeholder(value: str) -> bool:
    """True if the value still contains a REPLACE_WITH placeholder."""
    return "REPLACE_WITH" in (value or "")


def instagram_configured() -> bool:
    return not is_placeholder(INSTAGRAM_URL)


def email_configured() -> bool:
    return not is_placeholder(CONTACT_EMAIL)


def setup_problems() -> list[str]:
    """Human-readable list of details that still need to be filled in."""
    problems: list[str] = []
    if not instagram_configured():
        problems.append("INSTAGRAM_URL and INSTAGRAM_LABEL")
    if not email_configured():
        problems.append("CONTACT_EMAIL")
    if not (BASE_DIR / PORTRAIT_PATH).is_file():
        problems.append(f"portrait photo ({PORTRAIT_PATH})")
    return problems


def current_year() -> int:
    return date.today().year
