from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from clio.utils import generate_slug
from django.apps import apps
from django.core.validators import RegexValidator

# Create your models here.
def generate_profile_slug():
    model = apps.get_model(app_label='generalsettings', model_name='Profile')
    return generate_slug(model)


class Album(models.Model):

    url_regex = RegexValidator(
        regex=r'^[\w-]{5,15}$',
        message="Vanity url must be at least 5 characters, most 15 characters"
    )

    owner = models.OneToOneField(User)
    cover = models.ImageField(upload_to='album_covers')
    title = models.CharField(max_length=100, blank=False)
    slug = models.CharField(default=generate_profile_slug, blank=True, validators=[url_regex], max_length=15, unique=True)

    def __unicode__(self):
        return self.title


class Photo(models.Model):
    image = models.ImageField(upload_to='photos')
    album = models.ForeignKey(Album, related_name='photos')


class Transaction(models.Model):

    MODE_OF_DELIVERY = (
        (1, "Delivery"),
        (2, "Pick Up")
    )

    client = models.ForeignKey(User)
    contact_number = models.CharField(max_length=20, blank=False)
    shipping_address = models.TextField(blank=True)
    payable = models.IntegerField(blank=False, default=0)
    mode = models.IntegerField(choices=MODE_OF_DELIVERY)
