# -*- coding: utf-8 -*-
from django.db import models


# -----------------------------------------------------------------------------
# field mixins

class ColorMixin(object):

    """Adds color field to model."""

    color = models.CharField('color')


class SizeMixin(object):

    """Adds size field to model."""

    size = models.PositiveIntegerField('size')


# -----------------------------------------------------------------------------
# models

class Laptop(models.Model):

    """
    Laptop.

    laptop = Laptop(processor='1.2 GHz', ram='8 Gb')
    """

    processor = models.CharField('processor')
    ram = models.CharField('ram')


class TShirt(
    SizeMixin,
    ColorMixin,
    models.Model
):

    """
    TShirt.

    t_shirt = TShirt(size=20, color='blue')
    """

    pass


class TV(SizeMixin, models.Model):

    """
    TV.

    tv = TV(size=20, color='blue')
    """

    resolution = models.CharField('resolution')


class Pant(ColorMixin, models.Model):

    """
    Pant.

    pant = Pant(waist='some_value', length=20, color='blue')
    """

    waist = models.CharField('waist')
    length = models.PositiveIntegerField('length')
