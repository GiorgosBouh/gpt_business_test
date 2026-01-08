import csv
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from questionnaire_storage import FIELDNAMES, append_response_csv


def read_csv_rows(csv_path):
    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def test_append_response_csv_writes_header_and_rows(tmp_path):
    csv_path = tmp_path / "responses.csv"
    append_response_csv(
        {
            "name": "Ada",
            "role": "Professional",
            "experience": 5,
            "favorite_tool": "Python",
            "newsletter": "Yes",
        },
        csv_path=csv_path,
    )

    rows = read_csv_rows(csv_path)
    assert rows == [
        {
            "name": "Ada",
            "role": "Professional",
            "experience": "5",
            "favorite_tool": "Python",
            "newsletter": "Yes",
        }
    ]

    append_response_csv(
        {
            "name": "Grace",
            "role": "Manager",
            "experience": 12,
            "favorite_tool": "Spreadsheet",
            "newsletter": "No",
        },
        csv_path=csv_path,
    )

    rows = read_csv_rows(csv_path)
    assert rows == [
        {
            "name": "Ada",
            "role": "Professional",
            "experience": "5",
            "favorite_tool": "Python",
            "newsletter": "Yes",
        },
        {
            "name": "Grace",
            "role": "Manager",
            "experience": "12",
            "favorite_tool": "Spreadsheet",
            "newsletter": "No",
        },
    ]


def test_append_response_csv_fills_missing_fields(tmp_path):
    csv_path = tmp_path / "responses.csv"
    append_response_csv({"name": "Sam"}, csv_path=csv_path)

    rows = read_csv_rows(csv_path)
    assert rows == [
        {
            "name": "Sam",
            "role": "",
            "experience": "",
            "favorite_tool": "",
            "newsletter": "",
        }
    ]


def test_append_response_csv_fieldnames_constant():
    assert FIELDNAMES == ["name", "role", "experience", "favorite_tool", "newsletter"]