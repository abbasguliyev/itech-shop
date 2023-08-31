from django.db import models
from django.utils.translation import gettext_lazy as _

class DiscountType(models.TextChoices):
    FIXED = "fixed", _("FİX")
    PERCENTAGE = "percentage", _("FAİZ")