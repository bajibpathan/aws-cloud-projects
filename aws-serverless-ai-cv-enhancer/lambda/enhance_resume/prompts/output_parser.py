def parse_enhanced_bullets(
    generated_text: str
) -> list[str]:
    """
    Convert the model response into individual resume bullets.
    """

    bullets = []

    for line in generated_text.splitlines():

        cleaned_line = line.strip()

        if not cleaned_line:
            continue

        if cleaned_line.startswith("###"):
            continue

        if cleaned_line.startswith("- "):
            cleaned_line = cleaned_line[2:].strip()

        if cleaned_line:
            bullets.append(cleaned_line)

    return bullets