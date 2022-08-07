from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField("Наименование", max_length=256)
    slug = models.SlugField("Метка", unique=True, max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField("Наименование", max_length=100)
    slug = models.SlugField("Метка", unique=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField("Название", max_length=100)
    year = models.IntegerField("Год выпуска")
    description = models.TextField("Описание")
    rating = models.PositiveSmallIntegerField(
        verbose_name="Рейтинг", null=True, default=None
    )
    genre = models.ManyToManyField(Genre, verbose_name="Жанры")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="titles",
        verbose_name="Категория",
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"

    def __str__(self):
        return f"{self.category}: {self.name}"


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Произведение",
    )
    text = models.TextField("Текст отзыва")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Автор",
    )
    score = models.PositiveSmallIntegerField(
        verbose_name="Оценка",
        validators=[
            MinValueValidator(1, "Оценка не может быть меньше 1"),
            MaxValueValidator(10, "Оценка не может быть выше 10"),
        ],
    )
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["title", "author"], name="unique_title_author"
            )
        ]
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.author.username} - {self.text[:30]}"


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Отзыв",
    )
    text = models.TextField("Текст комментария")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="review",
        verbose_name="Автор",
    )
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.author} - {self.text[:30]}"
