
from django.db.models import CharField, TextField, DateTimeField, Model, ManyToManyField, ForeignKey, CASCADE

# Create your models here.

class Author(Model):
    fullname = CharField(max_length=50)
    born_date = CharField(max_length=50)
    born_location = CharField(max_length=200)
    description = TextField()
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class Tag(Model):
    name = CharField(max_length=30, null=False, unique=True)

    def __str__(self):
        return self.name


class Quote(Model):
    quote = TextField()
    tags = ManyToManyField(Tag)
    author = ForeignKey(Author, on_delete=CASCADE, default=None, null=True)
    creates_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote