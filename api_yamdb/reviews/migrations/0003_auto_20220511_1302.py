from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_auto_20220509_1845"),
    ]

    operations = [
        migrations.AddField(
            model_name="title",
            name="rating",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="genre",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="title",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
