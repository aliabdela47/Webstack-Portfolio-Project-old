# Generated by Django 4.2.3 on 2023-09-15 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablefile',
            name='prosecutor',
            field=models.CharField(max_length=255, verbose_name='ጉዳዩን የያዘው ዐቃቤ ህግ ስም'),
        ),
        migrations.AlterField(
            model_name='tablefile',
            name='status',
            field=models.CharField(max_length=255, verbose_name='በፍ/ቤቱ ውሳኔ መሰረት ተፈፅሞል/አልተፈፀመም'),
        ),
    ]