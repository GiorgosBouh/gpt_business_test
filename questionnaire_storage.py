from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class QuestionnaireStorage:
    responses: List[Dict[str, str]] = field(default_factory=list)

    def add_response(self, response: Dict[str, str]) -> None:
        self.responses.append(dict(response))

    def list_responses(self) -> List[Dict[str, str]]:
        return list(self.responses)
