from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

DEGREE_CHOICES = (
    ("Associate", "Associate"),
    ("Bachelor's", "Bachelor's"),
    ("Master's", "Master's"),
    ("Doctoral", "Doctoral"),
)


class City(models.Model):
    objects = models.Manager()
    city = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()
    country = models.CharField(max_length=50)
    iso2 = models.CharField(max_length=10)
    admin_name = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)
    population = models.BigIntegerField(blank=True, null=True)
    population_proper = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.city


def validate_resume_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError(u'Only pdf is supported')


def validate_photo_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.png', '.gif', '.jpeg', '.jpg']
    if ext not in valid_extensions:
        raise ValidationError(u'Image extension is not supported!')


class Registration(models.Model):
    objects = models.Manager()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    phone_number = PhoneNumberField(max_length=33)
    short_introduction = models.CharField(max_length=100)
    age = models.FloatField()
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    field_of_study = models.TextField()
    degree = models.TextField(choices=DEGREE_CHOICES)
    years_of_experience = models.FloatField()
    photo = models.ImageField(upload_to='files/photos/', validators=[validate_photo_extension])
    resume = models.FileField(upload_to='files/resumes/', validators=[validate_resume_extension])

    def __str__(self):
        return self.first_name
