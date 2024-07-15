# Generated by Django 4.2.11 on 2024-04-16 22:05

from django.db import migrations, models
import django.db.models.deletion
import django_choices_field.fields
import shelters.enums


class Migration(migrations.Migration):
    dependencies = [
        ("organizations", "0006_alter_organization_slug"),
        ("shelters", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="shelter",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="organizations.organization",
            ),
        ),
        migrations.AlterField(
            model_name="population",
            name="title",
            field=django_choices_field.fields.TextChoicesField(
                choices=[
                    ("Adults", "Adults"),
                    ("Men", "Men"),
                    ("Women", "Women"),
                    ("Families", "Families"),
                    ("Youth (TAY)", "Youth (TAY)"),
                    ("Boys", "Boys"),
                    ("Girls", "Girls"),
                    ("Seniors (55+)", "Seniors (55+)"),
                    ("Veterans", "Veterans"),
                    ("LGBTQ", "LGBTQ"),
                    ("HIV/AIDS", "HIV/AIDS"),
                ],
                choices_enum=shelters.enums.PopulationChoices,
                max_length=13,
            ),
        ),
        migrations.AlterField(
            model_name="requirement",
            name="title",
            field=django_choices_field.fields.TextChoicesField(
                choices=[
                    ("Photo ID", "Photo ID"),
                    ("Medicaid or Medicare", "Medicaid or Medicare"),
                    ("Veteran", "Veteran"),
                    ("Reservation", "Reservation"),
                    ("Referral", "Referral"),
                    ("Wheelchair Accessibel", "Wheelchair Accessible"),
                    ("Medical Equipment Permitted", "Medical Equipment Permitted"),
                    ("Pets Allowed", "Pets Allowed"),
                ],
                choices_enum=shelters.enums.EntryRequirementChoices,
                max_length=27,
            ),
        ),
        migrations.AlterField(
            model_name="shelter",
            name="spa",
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="SPA"),
        ),
        migrations.CreateModel(
            name="Funder",
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
                (
                    "title",
                    django_choices_field.fields.TextChoicesField(
                        choices=[
                            ("MPP", "MPP"),
                            ("LAHSA", "LAHSA"),
                            ("DMH", "DMH"),
                            ("DHS", "DHS"),
                        ],
                        choices_enum=shelters.enums.FunderChoices,
                        max_length=5,
                    ),
                ),
                (
                    "shelter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="funders",
                        to="shelters.shelter",
                    ),
                ),
            ],
        ),
    ]
