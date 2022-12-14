import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10)),
                ("slug", models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10)),
                ("slug", models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name="title",
            name="description",
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="title",
            name="name",
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="title",
            name="year",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="title",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="titles",
                to="reviews.Category",
            ),
        ),
        migrations.AddField(
            model_name="title",
            name="genre",
            field=models.ManyToManyField(
                related_name="titles", to="reviews.Genre"
            ),
        ),
    ]
