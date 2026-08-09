import json
from typing import Any
"""
Request validation for the Serverless AI CV Enhancer.
"""

MAX_JOB_DESCRIPTION_LENGTH = 10000
MAX_RESUME_BULLETS = 20
MAX_BULLET_LENGTH = 1000


def validate_request(request_body):
    """
    Validate the incoming request payload.

    Returns:
        None if valid, otherwise an error message.
    """

    job_description = request_body.get("jobDescription")

    if job_description is None:
        return "Job description is required."

    if not isinstance(job_description, str):
        return "Job description must be a string."

    if not job_description.strip():
        return "Job description cannot be empty."

    if len(job_description) > MAX_JOB_DESCRIPTION_LENGTH:
        return (
            f"Job description cannot exceed "
            f"{MAX_JOB_DESCRIPTION_LENGTH} characters."
        )

    resume_bullets = request_body.get("resumeBullets")

    if resume_bullets is None:
        return "Resume bullets are required."

    if not isinstance(resume_bullets, list):
        return "Resume bullets must be a list."

    if len(resume_bullets) == 0:
        return "Resume bullets cannot be empty."

    if len(resume_bullets) > MAX_RESUME_BULLETS:
        return (
            f"Resume bullets cannot exceed "
            f"{MAX_RESUME_BULLETS} items."
        )

    for bullet in resume_bullets:

        if not isinstance(bullet, str):
            return "Each resume bullet must be a string."

        if not bullet.strip():
            return "Resume bullets cannot contain empty values."

        if len(bullet) > MAX_BULLET_LENGTH:
            return (
                f"Each resume bullet cannot exceed "
                f"{MAX_BULLET_LENGTH} characters."
            )

    return None