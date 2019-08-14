from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel
from user.models import User

class Product(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100, null=True, blank=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='products/', null=True, blank=True)
    description = models.CharField(verbose_name=_('Description'), max_length=1000, null=True, blank=True)
    amount_of_quantites = models.PositiveIntegerField(verbose_name=_('Amount Of Quantites'), default=0)
    unit_price = models.DecimalField(verbose_name=_('Unit price'), max_digits=10, decimal_places=6,
                                    null=True, blank=True)
    seller = models.ForeignKey(to='user.User', verbose_name=_('Seller'), related_name='products', 
                                    on_delete=models.CASCADE, null=True, blank=True)
    
    
    def __str__(self):
        return self.name