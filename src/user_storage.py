import json
from pathlib import Path


class UserMemoryStorage:
    """Persistent storage for separate user memories."""

    def __init__(self, base_path: str = "data/users") -> None:
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def _file(self, user_id: str) -> Path:
        return self.base_path / f"{user_id}.json"

    def save(self, user_id: str, data: dict) -> None:
        self._file(user_id).write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def load(self, user_id: str) -> dict:
        path = self._file(user_id)
        if not path.exists():
            return {}
        return json.loads(path.read_text(encoding="utf-8"))
