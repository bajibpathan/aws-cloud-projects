import json
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_DIR))

from normalizer import normalize_portfolio
from validators import validate_portfolio


def test_sample_ai_output() -> None:
    test_file = Path(__file__).parent / "sample-ai-output.json"

    with test_file.open("r", encoding="utf-8") as file:
        source_document = json.load(file)

    portfolio_data = normalize_portfolio(source_document)

    validate_portfolio(portfolio_data)

    assert (
        portfolio_data["personal_information"]["full_name"]
        == "Alex Morgan"
    )

    assert (
        portfolio_data["personal_information"]["linkedin"]
        == "https://linkedin.com/in/alexmorgan"
    )

    assert "AWS Lambda" in portfolio_data["skills"]

    assert len(portfolio_data["experience"]) == 1
    assert len(portfolio_data["certifications"]) == 2
    assert len(portfolio_data["projects"]) == 1