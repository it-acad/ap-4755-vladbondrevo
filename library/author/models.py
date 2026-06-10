from django.db import models

class Author(models.Model):
    # Додаємо поля бази даних
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.surname} {self.patronymic}"

    def __repr__(self):
        return f"Author(id={self.id}, name='{self.name}', surname='{self.surname}')"

    @staticmethod
    def get_by_id(author_id):
        try:
            return Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return None

    @staticmethod
    def delete_by_id(author_id):
        author = Author.get_by_id(author_id)
        if author:
            author.delete()
            return True
        return False

    @staticmethod
    def create(name, surname, patronymic):
        return Author.objects.create(name=name, surname=surname, patronymic=patronymic)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'patronymic': self.patronymic,
        }

    def update(self, name=None, surname=None, patronymic=None):
        if name: self.name = name
        if surname: self.surname = surname
        if patronymic: self.patronymic = patronymic
        self.save()

    @staticmethod
    def get_all():
        return Author.objects.all()