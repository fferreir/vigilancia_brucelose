# Generated by Django 5.1.5 on 2025-05-04 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("brutb", "0002_rename_propriedades_propriedade"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="brasil",
            options={"ordering": ["cd_uf", "nm_mun"]},
        ),
        migrations.AddIndex(
            model_name="brasil",
            index=models.Index(
                fields=["cd_uf", "nm_mun"], name="brutb_brasi_cd_uf_1d7898_idx"
            ),
        ),
    ]
