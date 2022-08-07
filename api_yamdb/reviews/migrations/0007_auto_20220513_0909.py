from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0006_merge_20220511_1720"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="title",
            options={"ordering": ("name",)},
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name="genre",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
