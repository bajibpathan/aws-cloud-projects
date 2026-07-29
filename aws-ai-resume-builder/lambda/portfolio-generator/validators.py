from __future__ import annotations

from typing import Any


SUPPORTED_SCHEMA_VERSIONS = {"1.0"}


def validate_portfolio(portfolio_data: dict[str, Any]) -> None:
    """
    Validate the normalized portfolio data.

    Raises ValueError when required fields are missing or invalid.
    """
    schema_version = portfolio_data.get("schema_version", "1.0")

    if schema_version not in SUPPORTED_SCHEMA_VERSIONS:
        raise ValueError(
            f"Unsupported portfolio schema version: {schema_version}"
        )

    personal_information = portfolio_data.get(
        "personal_information"
    )

    if not isinstance(personal_information, dict):
        raise ValueError(
            "personal_information must be a JSON object."
        )

    full_name = personal_information.get("full_name")

    if not isinstance(full_name, str) or not full_name.strip():
        raise ValueError(
            "personal_information.full_name is required."
        )

    professional_summary = portfolio_data.get(
        "professional_summary"
    )

    if not isinstance(professional_summary, str):
        raise ValueError(
            "professional_summary must be a string."
        )

    list_fields = [
        "skills",
        "experience",
        "education",
        "certifications",
        "projects",
    ]

    for field_name in list_fields:
        if not isinstance(portfolio_data.get(field_name), list):
            raise ValueError(
                f"{field_name} must be a list."
            )