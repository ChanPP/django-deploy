from django.db import models

# Create your models here.
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Photo(models.Model):
    file = models.ImageField(upload_to='photo', blank=True)


@receiver(pre_delete, sender=Photo)
def remove_file_from_s3(sender, instance, **kwagrs):
    instance.file.delete(save=False)
