from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_auto_20220509_1845"),
    ]

    operations = [
        migrations.AlterField(
            model_name="title",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
