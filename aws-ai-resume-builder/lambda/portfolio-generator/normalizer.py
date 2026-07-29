from __future__ import annotations

from typing import Any
from urllib.parse import urlparse


def normalize_url(value: Any) -> str:
    """
    Normalize an external URL.

    Adds https:// when the value contains a domain but no URL scheme.
    Returns an empty string when the value is missing or invalid.
    """
    if not isinstance(value, str):
        return ""

    url = value.strip()

    if not url:
        return ""

    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"

    parsed_url = urlparse(url)

    if parsed_url.scheme not in {"http", "https"}:
        return ""

    if not parsed_url.netloc:
        return ""

    return url


def normalize_string(value: Any) -> str:
    """Return a clean string or an empty string."""
    if value is None:
        return ""

    if not isinstance(value, str):
        return str(value).strip()

    return value.strip()


def normalize_list(value: Any) -> list:
    """Return the value when it is a list, otherwise return an empty list."""
    return value if isinstance(value, list) else []


def normalize_personal_information(data: Any) -> dict[str, str]:
    """Normalize personal-information fields."""
    if not isinstance(data, dict):
        data = {}

    return {
        "full_name": normalize_string(data.get("full_name")),
        "professional_title": normalize_string(
            data.get("professional_title")
        ),
        "email": normalize_string(data.get("email")),
        "phone": normalize_string(data.get("phone")),
        "location": normalize_string(data.get("location")),
        "linkedin": normalize_url(data.get("linkedin")),
        "github": normalize_url(data.get("github")),
        "website": normalize_url(data.get("website")),
    }


def normalize_experience(items: Any) -> list[dict[str, Any]]:
    """Normalize professional experience records."""
    normalized_items = []

    for item in normalize_list(items):
        if not isinstance(item, dict):
            continue

        normalized_items.append(
            {
                "job_title": normalize_string(item.get("job_title")),
                "company": normalize_string(item.get("company")),
                "location": normalize_string(item.get("location")),
                "start_date": normalize_string(item.get("start_date")),
                "end_date": normalize_string(item.get("end_date")),
                "responsibilities": [
                    normalize_string(responsibility)
                    for responsibility in normalize_list(
                        item.get("responsibilities")
                    )
                    if normalize_string(responsibility)
                ],
            }
        )

    return normalized_items


def normalize_education(items: Any) -> list[dict[str, str]]:
    """Normalize education records."""
    normalized_items = []

    for item in normalize_list(items):
        if not isinstance(item, dict):
            continue

        normalized_items.append(
            {
                "degree": normalize_string(
                    item.get("degree") or item.get("qualification")
                ),
                "institution": normalize_string(item.get("institution")),
                "location": normalize_string(item.get("location")),
                "graduation_date": normalize_string(
                    item.get("graduation_date")
                    or item.get("completion_date")
                ),
            }
        )

    return normalized_items


def normalize_certifications(items: Any) -> list[dict[str, str]]:
    """Normalize certification records."""
    normalized_items = []

    for item in normalize_list(items):
        if not isinstance(item, dict):
            continue

        normalized_items.append(
            {
                "name": normalize_string(item.get("name")),
                "issuer": normalize_string(item.get("issuer")),
                "date": normalize_string(item.get("date")),
                "credential_url": normalize_url(
                    item.get("credential_url")
                ),
            }
        )

    return normalized_items


def normalize_projects(items: Any) -> list[dict[str, Any]]:
    """Normalize project records."""
    normalized_items = []

    for item in normalize_list(items):
        if not isinstance(item, dict):
            continue

        project_url = (
            item.get("project_url")
            or item.get("repository_url")
            or item.get("url")
        )

        normalized_items.append(
            {
                "name": normalize_string(item.get("name")),
                "description": normalize_string(
                    item.get("description")
                ),
                "technologies": [
                    normalize_string(technology)
                    for technology in normalize_list(
                        item.get("technologies")
                    )
                    if normalize_string(technology)
                ],
                "url": normalize_url(project_url),
            }
        )

    return normalized_items


def normalize_portfolio(source_document: dict[str, Any]) -> dict[str, Any]:
    """
    Convert an AI Resume Analyzer output document into the internal
    portfolio data model.
    """
    if not isinstance(source_document, dict):
        raise ValueError("AI output must be a JSON object.")

    if source_document.get("status") != "COMPLETED":
        raise ValueError(
            "AI analysis is not in COMPLETED status."
        )

    resume_data = source_document.get("resume")

    if not isinstance(resume_data, dict):
        raise ValueError(
            "AI output does not contain a valid resume object."
        )

    skills = [
        normalize_string(skill)
        for skill in normalize_list(resume_data.get("skills"))
        if normalize_string(skill)
    ]

    normalized_portfolio = {
        "schema_version": source_document.get(
            "schema_version",
            "1.0"
        ),
        "personal_information": normalize_personal_information(
            resume_data.get("personal_information")
        ),
        "professional_summary": normalize_string(
            resume_data.get("professional_summary")
        ),
        "skills": skills,
        "experience": normalize_experience(
            resume_data.get("experience")
        ),
        "education": normalize_education(
            resume_data.get("education")
        ),
        "certifications": normalize_certifications(
            resume_data.get("certifications")
        ),
        "projects": normalize_projects(
            resume_data.get("projects")
        ),
    }

    return normalized_portfolio