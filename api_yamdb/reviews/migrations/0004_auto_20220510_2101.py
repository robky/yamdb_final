from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0003_auto_20220510_1314"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="review_id",
            new_name="review",
        ),
        migrations.RenameField(
            model_name="review",
            old_name="title_id",
            new_name="title",
        ),
    ]
