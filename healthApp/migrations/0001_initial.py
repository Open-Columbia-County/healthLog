# Generated by Django 4.0.5 on 2022-10-28 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('read', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('freq', models.CharField(default='daily', max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(max_length=255)),
                ('info', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('level', models.IntegerField(default=0)),
                ('loggedOn', models.DateTimeField(auto_now=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theWriter', to='healthApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='med.jpg', upload_to='medicationImgs')),
                ('medication', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='healthApp.medication')),
            ],
        ),
        migrations.CreateModel(
            name='Taken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('dose', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('day', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='theDay', to='healthApp.log')),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theMed', to='healthApp.medication')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserTaken', to='healthApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Sugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('level', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('note', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='theNote', to='healthApp.log')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theOwner', to='healthApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replyTo', to='healthApp.comment')),
                ('replyFromUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userFromReply', to='healthApp.user')),
                ('replyToUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userToReply', to='healthApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='bee.jpg', upload_to='profileImgs')),
                ('diabetic', models.BooleanField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='healthApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thePatient', to='healthApp.user')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theDr', to='healthApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aboutUser', to='healthApp.user')),
                ('dr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drNote', to='healthApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('mood', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('log', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='theLog', to='healthApp.log')),
                ('symptom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theSymptom', to='healthApp.symptom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserMood', to='healthApp.user')),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theAuthor', to='healthApp.user'),
        ),
        migrations.AddField(
            model_name='log',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theWeek', to='healthApp.week'),
        ),
        migrations.AddField(
            model_name='comment',
            name='fromUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userFrom', to='healthApp.user'),
        ),
        migrations.AddField(
            model_name='comment',
            name='toUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userTo', to='healthApp.user'),
        ),
    ]
