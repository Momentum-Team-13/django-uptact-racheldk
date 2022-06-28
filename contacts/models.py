from django.db import models
from django.core.validators import RegexValidator
from localflavor.us.models import USStateField, USZipCodeField
from django.utils import timezone


class Note(models.Model):
    note_content = models.TextField(blank=True, null=True)
    note_date = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?\d{10}$',
        message="Phone number must be entered in the format: '+9999999999'.")

    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11,
                                    validators=[phone_regex],
                                    null=True,
                                    blank=True)
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    zip_code = USZipCodeField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="note", blank=True, null=True)
# null=True means that the value is allowed to be null, same for blank=True





