from django.db import models
from config.models import BasedModel

class CertificationCard(BasedModel):
    card_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    iqama_id = models.CharField(max_length=20)
    certified_level = models.CharField(max_length=50)
    model_level = models.CharField(max_length=50)
    issued_on = models.DateField()
    valid_until = models.DateField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
