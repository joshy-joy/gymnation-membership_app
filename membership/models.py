from django.db import models
from django.core.validators import EmailValidator

class MembershipPlans(models.Model):
    duration = models.PositiveIntegerField()  # Duration in days/months/years
    access_level = models.CharField(max_length=100)
    price_tier = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.access_level} ({self.price_tier})"

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()], unique=True)
    password = models.CharField(max_length=128)  # Typically hashed passwords
    membership_type = models.ForeignKey(MembershipPlans, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class Trainer(models.Model):
    specialization = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)  # For example: "Mon-Fri 9AM-5PM"

    def __str__(self):
        return self.specialization

class CheckIns(models.Model):
    updated_time = models.DateTimeField(auto_now=True)  # Automatically updates on each save
    location = models.CharField(max_length=255)
    session_type = models.CharField(max_length=100)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return f"Check-in at {self.location} ({self.session_type})"

class MemberTrainerMapping(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member} assigned to {self.trainer}"
