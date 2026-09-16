import json
from pathlib import Path


class SessionStorage:
    """Persistent storage for isolated user conversation sessions."""

    def __init__(self, path: str = "data/sessions") -> None:
        self.path = Path(path)
        self.path.mkdir(parents=True, exist_ok=True)

    def _file(self, user_id: str) -> Path:
        return self.path / f"{user_id}.json"

    def save(self, user_id: str, messages: list) -> None:
        self._file(user_id).write_text(
            json.dumps(messages, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def load(self, user_id: str) -> list:
        file = self._file(user_id)
        if not file.exists():
            return []

        return json.loads(file.read_text(encoding="utf-8"))
