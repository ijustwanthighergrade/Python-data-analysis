# Generated by Django 4.1.4 on 2023-12-19 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarriageSurvey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('gender', models.CharField(max_length=10)),
                ('education', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_married', models.BooleanField()),
                ('marriage_intention', models.CharField(max_length=255)),
                ('agree_buying_house', models.BooleanField()),
                ('buying_house_influence', models.IntegerField()),
                ('marriage_house_requirement', models.IntegerField()),
                ('afford_house_price', models.IntegerField()),
                ('buying_house_impact_life', models.IntegerField()),
                ('government_support', models.IntegerField()),
                ('family_planning', models.IntegerField()),
                ('desire_for_children', models.IntegerField()),
                ('legal_recognition', models.IntegerField()),
                ('tradition', models.IntegerField()),
                ('responsibility_sharing', models.IntegerField()),
                ('sacrifice_lifestyle', models.IntegerField()),
                ('affordability', models.IntegerField()),
                ('marriage_expenses_affordability', models.IntegerField()),
                ('stable_career_before_family', models.IntegerField()),
                ('child_rearing_cost_affordability', models.IntegerField()),
                ('non_economic_factor_relationship', models.IntegerField()),
                ('family_adjustment_concerns', models.IntegerField()),
                ('trustworthiness', models.IntegerField()),
                ('fear_of_commitment', models.IntegerField()),
                ('freedom_loss_after_marriage', models.IntegerField()),
                ('no_partner', models.IntegerField()),
                ('fear_of_marriage_failure', models.IntegerField()),
            ],
        ),
    ]
