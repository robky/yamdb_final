from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0007_auto_20220513_0909"),
    ]

    operations = [
        migrations.AlterField(
            model_name="title",
            name="genre",
            field=models.ManyToManyField(to="reviews.Genre"),
        ),
    ]
