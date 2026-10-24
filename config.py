
"""Central configuration for Azerbaijani with Rashida."""

from dataclasses import dataclass


@dataclass(frozen=True)
class BrandConfig:
    teacher_name: str = "Rashida"
    brand_name: str = "Azerbaijani with Rashida"

    website_title: str = (
        "Azerbaijani with Rashida | Learn Azerbaijani Online"
    )
    meta_description: str = (
        "Learn Azerbaijani with Rashida through practical conversations, "
        "everyday expressions, and cultural insights."
    )

    # Replace these two placeholders with real contact details.
    instagram_url: str = (
        "https://www.instagram.com/REPLACE_WITH_INSTAGRAM_HANDLE/"
    )
    contact_email: str = (
        "REPLACE_WITH_CONTACT_EMAIL@example.com"
    )

    # Add Rashida's approved portrait at this path.
    portrait_path: str = "assets/images/rashida-portrait.jpg"

    # Brand colors
    primary: str = "#6C3CE9"
    deep: str = "#32145F"
    yellow: str = "#FFD84D"
    white: str = "#FFFFFF"
    lavender: str = "#F3EEFF"
    ink: str = "#211936"

    # Contact forms do not send or store submissions by default.
    contact_form_enabled: bool = False


BRAND = BrandConfig()
