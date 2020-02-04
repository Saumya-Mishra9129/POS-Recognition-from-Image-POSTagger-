from django.db import models


class ImagesPos(models.Model):
    photo = models.ImageField()

    class Meta:
        verbose_name_plural="Images"
    def __str__(self):
        return self.photo