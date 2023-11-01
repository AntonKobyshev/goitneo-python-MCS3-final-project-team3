from models.Field import Field


class Notes(Field):
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __str__(self):
        return f"📝 Note title: {self.title}, text: {self.text}"
