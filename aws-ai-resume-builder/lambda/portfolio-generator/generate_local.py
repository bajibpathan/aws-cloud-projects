from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

from normalizer import normalize_portfolio
from renderer import read_portfolio_css, render_portfolio_html
from validators import validate_portfolio


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT_FILE = BASE_DIR / "tests" / "sample-ai-output.json"
OUTPUT_DIR = BASE_DIR / "generated"


def load_json_file(file_path: Path) -> dict:
    """
    Load a JSON file and return its contents.
    """
    if not file_path.exists():
        raise FileNotFoundError(
            f"Input JSON file not found: {file_path}"
        )

    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError(
            "The input JSON must contain a JSON object."
        )

    return data


def generate_local_portfolio(
    input_file: Path,
    output_directory: Path,
) -> None:
    """
    Generate the portfolio website locally.
    """
    source_document = load_json_file(input_file)

    portfolio_data = normalize_portfolio(source_document)

    validate_portfolio(portfolio_data)

    rendered_html = render_portfolio_html(portfolio_data)
    stylesheet = read_portfolio_css()

    output_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    html_output = output_directory / "index.html"
    css_output = output_directory / "style.css"
    json_output = output_directory / "portfolio.json"

    html_output.write_text(
        rendered_html,
        encoding="utf-8",
    )

    css_output.write_text(
        stylesheet,
        encoding="utf-8",
    )

    json_output.write_text(
        json.dumps(
            portfolio_data,
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print("Portfolio generated successfully.")
    print(f"HTML: {html_output}")
    print(f"CSS:  {css_output}")
    print(f"JSON: {json_output}")


def main() -> None:
    """
    Run local portfolio generation.

    An optional JSON file path can be supplied:

        python generate_local.py path/to/input.json
    """
    input_file = DEFAULT_INPUT_FILE

    if len(sys.argv) > 1:
        input_file = Path(sys.argv[1]).expanduser().resolve()

    generate_local_portfolio(
        input_file=input_file,
        output_directory=OUTPUT_DIR,
    )


if __name__ == "__main__":
    main()