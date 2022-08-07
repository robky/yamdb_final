from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователей
    """

    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        required=True,
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "bio",
            "role",
        )
        model = User


class UserEditSerializer(serializers.ModelSerializer):
    """
    Сериализатор редактирования пользователей
    """

    class Meta:
        exclude = ("id",)
        model = User
        read_only_fields = ("role",)


class RegisterDataSerializer(serializers.ModelSerializer):
    """
    Сериализатор регистрации
    """

    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        fields = ("username", "email")
        model = User

    def validate_username(self, value):
        if value.lower() == "me":
            raise serializers.ValidationError("Username 'me' is not valid")
        return value


class TokenSerializer(serializers.Serializer):
    """
    Сериализатор токена
    """

    username = serializers.CharField()
    confirmation_code = serializers.CharField()


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        model = Review
        exclude = ("title",)

    def validate(self, data):
        if self.context["request"].method == "POST":
            user = self.context["request"].user
            my_view = self.context["view"]
            title_id = my_view.kwargs.get("title_id")
            title = get_object_or_404(Title, id=title_id)
            if title.reviews.filter(author=user).exists():
                raise serializers.ValidationError(["Уже есть отзыв"])
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        model = Comment
        exclude = ("review",)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ("id",)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ("id",)


class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра произведений."""

    genre = GenreSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Title
        fields = "__all__"


class TitleCreateSerializer(serializers.ModelSerializer):
    """Сериализатор создания произведений."""

    genre = serializers.SlugRelatedField(
        slug_field="slug", many=True, queryset=Genre.objects.all()
    )

    category = serializers.SlugRelatedField(
        slug_field="slug", queryset=Category.objects.all()
    )

    class Meta:
        model = Title
        fields = "__all__"
