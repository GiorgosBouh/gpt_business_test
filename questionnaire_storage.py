from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List

import csv


@dataclass
class QuestionnaireStorage:
    responses: List[Dict[str, str]] = field(default_factory=list)
    storage_path: Path = field(
        default_factory=lambda: Path(__file__).resolve().parent / "questionnaire_responses.csv"
    )

    def add_response(self, response: Dict[str, str]) -> None:
        response_copy = dict(response)
        self.responses.append(response_copy)

        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        file_exists = self.storage_path.exists()
        with self.storage_path.open("a", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(response_copy.keys()))
            if not file_exists:
                writer.writeheader()
            writer.writerow(response_copy)

    def list_responses(self) -> List[Dict[str, str]]:
        if self.storage_path.exists():
            with self.storage_path.open("r", newline="", encoding="utf-8") as handle:
                reader = csv.DictReader(handle)
                self.responses = [dict(row) for row in reader]
        return list(self.responses)

