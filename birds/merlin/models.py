from django.db import models

class Order(models.Model):
    name = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        unique=True
    )
    
    def __str__(self):
        return self.name


class Family(models.Model):
    name = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        unique=True
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='families'
    )

    def __str__(self):
        return self.name
    

class Bird(models.Model):
    common_name = models.CharField(
        max_length=256,
        unique=True
    )
    slug = models.SlugField(max_length=256)
    family = models.ForeignKey(
        Family,
        on_delete=models.CASCADE,
        related_name='birds',
        null=True,
        blank=True
    )
    genus = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    species = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    link = models.CharField(
        max_length=512,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.common_name


class Location(models.Model):
    name=models.CharField(
        max_length=256,
        unique=True
    )
    description=models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        ordering=['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name


class Detection(models.Model):
    date = models.DateField()
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='detections'
    )
    bird = models.ForeignKey(
        Bird,
        on_delete=models.CASCADE,
        related_name='detections'
    )

    def __str__(self):
        return f"{self.date}: {self.bird.common_name}, {self.location.name}"

    class Meta:
        indexes = [
            models.Index(fields=['date'])
        ]


