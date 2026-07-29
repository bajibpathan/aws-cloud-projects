from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from jinja2 import (
    Environment,
    FileSystemLoader,
    StrictUndefined,
    select_autoescape,
)


BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = BASE_DIR / "templates"


def create_jinja_environment() -> Environment:
    """
    Create and configure the Jinja2 template environment.

    StrictUndefined raises an error when the template references
    a field that does not exist. This helps detect template mistakes
    during development.
    """
    return Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=select_autoescape(
            enabled_extensions=("html", "xml"),
            default_for_string=True,
        ),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )


def render_portfolio_html(
    portfolio_data: dict[str, Any],
) -> str:
    """
    Render the portfolio data using the index.html Jinja2 template.

    Returns:
        Rendered HTML as a string.
    """
    environment = create_jinja_environment()
    template = environment.get_template("index.html")

    current_year = datetime.now(UTC).year

    return template.render(
        **portfolio_data,
        current_year=current_year,
    )


def read_portfolio_css() -> str:
    """
    Read and return the portfolio CSS template.

    The CSS does not currently contain dynamic Jinja2 fields,
    so it can be copied directly.
    """
    css_path = TEMPLATE_DIR / "style.css"

    if not css_path.exists():
        raise FileNotFoundError(
            f"Portfolio stylesheet not found: {css_path}"
        )

    return css_path.read_text(encoding="utf-8")