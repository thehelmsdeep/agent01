import json
from pathlib import Path


class MemoryStorage:
    """Simple persistent JSON storage for agent memories."""

    def __init__(self, path: str = "data/memory.json") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def save(self, data: dict) -> None:
        self.path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def load(self) -> dict:
        if not self.path.exists():
            return {}

        return json.loads(self.path.read_text(encoding="utf-8"))
