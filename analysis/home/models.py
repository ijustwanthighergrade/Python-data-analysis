# models.py
from django.db import models

class MarriageSurvey(models.Model):
    timestamp = models.DateTimeField()
    gender = models.CharField(max_length=10)
    education = models.CharField(max_length=50)
    age = models.CharField(max_length=10)  # Modify this based on your actual age data
    salary = models.CharField(max_length=50)
    is_married = models.CharField(max_length=3)  # Assuming "是" or "否"
    marriage_intention = models.IntegerField()
    agree_buying_house = models.IntegerField()
    buying_house_influence = models.IntegerField()
    marriage_house_requirement = models.IntegerField()
    afford_house_price = models.IntegerField()
    buying_house_impact_life = models.IntegerField()
    government_support = models.IntegerField()
    family_planning = models.IntegerField()
    desire_for_children = models.IntegerField()
    legal_recognition = models.IntegerField()
    tradition = models.IntegerField()
    responsibility_sharing = models.IntegerField()
    sacrifice_lifestyle = models.IntegerField()
    affordability = models.IntegerField()
    marriage_expenses_affordability = models.IntegerField()
    stable_career_before_family = models.IntegerField()
    child_rearing_cost_affordability = models.IntegerField()
    non_economic_factor_relationship = models.IntegerField()
    family_adjustment_concerns = models.IntegerField()
    trustworthiness = models.IntegerField()
    fear_of_commitment = models.IntegerField()
    freedom_loss_after_marriage = models.IntegerField()
    no_partner = models.IntegerField()
    fear_of_marriage_failure = models.IntegerField()
    anycommond = models.CharField(max_length=50, blank=True, null=True)  # Add blank=True, null=True to handle existing rows

    def __str__(self):
        return f"Marriage Survey - {self.timestamp}"