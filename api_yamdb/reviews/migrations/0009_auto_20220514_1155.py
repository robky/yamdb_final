from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0008_auto_20220513_0927"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="review",
            constraint=models.UniqueConstraint(
                fields=("title", "author"), name="unique_title_author"
            ),
        ),
    ]
