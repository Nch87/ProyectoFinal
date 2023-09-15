# Generated by Django 4.2.5 on 2023-09-14 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppInicio', '0004_avatar_remove_post_author_alter_adopcion_autor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ayuda',
            old_name='pub_date',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='ayuda',
            old_name='contenido',
            new_name='mensaje',
        ),
        migrations.RemoveField(
            model_name='ayuda',
            name='titulo',
        ),
        migrations.AddField(
            model_name='ayuda',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ayuda',
            name='nombre',
            field=models.CharField(default='example@example.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ayuda',
            name='telefono',
            field=models.CharField(default='11111111', max_length=20),
            preserve_default=False,
        ),
    ]
