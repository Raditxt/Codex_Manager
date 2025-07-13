import uuid
from datetime import datetime

class Entry:
    def __init__(self, title, category, tags, summary, code_snippet, source, date_created=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.category = category
        self.tags = tags
        self.summary = summary
        self.code_snippet = code_snippet
        self.source = source
        self.date_created = date_created or datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "category": self.category,
            "tags": self.tags,
            "summary": self.summary,
            "code_snippet": self.code_snippet,
            "source": self.source,
            "date_created": self.date_created
        }

    @staticmethod
    def from_dict(data):
        return Entry(
            title=data["title"],
            category=data["category"],
            tags=data["tags"],
            summary=data["summary"],
            code_snippet=data["code_snippet"],
            source=data["source"],
            date_created=data.get("date_created")
        )
