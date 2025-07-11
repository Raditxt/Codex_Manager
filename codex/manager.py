import json
import os
from codex.entry import Entry

class CodexManager:
    def __init__(self, filepath="data/entries.json"):
        self.filepath = filepath
        self.entries = []
        self.load()

    def add_entry(self, entry):
        self.entries.append(entry)
        self.save()

    def delete_entry(self, title):
        self.entries = [e for e in self.entries if e.title.lower() != title.lower()]
        self.save()

    def search_by_tag(self, tag):
        return [e for e in self.entries if tag.lower() in [t.lower() for t in e.tags]]

    def search_by_title(self, keyword):
        return [e for e in self.entries if keyword.lower() in e.title.lower()]

    def list_all(self):
        return self.entries
    
    def save(self):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump([e.to_dict() for e in self.entries], f, indent=4)

    def load(self):
        if not os.path.exists(self.filepath):
            self.entries = []
            return
        with open(self.filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.entries = [Entry.from_dict(d) for d in data]
