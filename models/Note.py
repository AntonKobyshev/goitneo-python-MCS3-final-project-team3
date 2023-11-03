from models.Field import Field

class Notes(Field):
    def __init__(self, title, text, tags=None):
        self.title = title
        self.text = text
        self.tags = set(tags) if tags else set()

    def add_tag(self, tag):
        self.tags.add(tag)

    def remove_tag(self, tag):
        self.tags.discard(tag)

    def __str__(self):
        tags_str = ', '.join(self.tags)
        return f"📝 Note title: {self.title}, text: {self.text}, tags: [{tags_str}]"