# Generated by Django 4.2 on 2023-04-28 13:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Date",
            fields=[
                (
                    "date_id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                (
                    "date",
                    models.DateField(default=django.utils.timezone.now, max_length=255),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="Victor", max_length=256)),
                ("reg_no", models.IntegerField(default=100)),
                ("period_1", models.BooleanField(default=False)),
                ("period_2", models.BooleanField(default=False)),
                ("period_3", models.BooleanField(default=False)),
                ("period_4", models.BooleanField(default=False)),
                ("period_5", models.BooleanField(default=False)),
                ("period_6", models.BooleanField(default=False)),
                ("period_7", models.BooleanField(default=False)),
                (
                    "log_date",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attendances",
                        to="Attendance.date",
                    ),
                ),
            ],
        ),
    ]
