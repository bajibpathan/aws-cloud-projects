from pathlib import Path

from config import PROMPT_VERSION


def load_prompt_template() -> str:
    """
    Load the approved resume enhancement prompt template.
    """

    current_file = Path(__file__).resolve()

    project_root = current_file.parents[3]

    prompt_file = (
        project_root
        / "prompts"
        / f"resume-enhancer-{PROMPT_VERSION}.txt"
    )

    return prompt_file.read_text(encoding="utf-8")


def build_prompt(
    job_description: str,
    resume_bullets: list[str]
) -> str:
    """
    Build the final prompt using the job description
    and resume bullets supplied by the user.
    """

    template = load_prompt_template()

    formatted_bullets = "\n".join(
        f"- {bullet}"
        for bullet in resume_bullets
    )

    prompt = template.replace(
        "{{JOB_DESCRIPTION}}",
        job_description
    )

    prompt = prompt.replace(
        "{{RESUME_BULLETS}}",
        formatted_bullets
    )

    return prompt