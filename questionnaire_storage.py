import csv
from pathlib import Path

FIELDNAMES = ["name", "role", "experience", "favorite_tool", "newsletter"]


def append_response_csv(response, csv_path=None):
    if csv_path is None:
        csv_path = Path(__file__).resolve().parent / "responses.csv"
    else:
        csv_path = Path(csv_path)

    needs_header = not csv_path.exists() or csv_path.stat().st_size == 0

    with csv_path.open("a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        if needs_header:
            writer.writeheader()
        writer.writerow({key: response.get(key, "") for key in FIELDNAMES})
