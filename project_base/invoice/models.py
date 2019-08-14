from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel
from base.constants import STATUS_CHOICE, PENDING

class Invoice(BaseModel):
    product = models.ForeignKey(to='product.Product', verbose_name=_('Product'), related_name='invoices',
                                    on_delete=models.CASCADE, null=True, blank=True)
    seller = models.ForeignKey(to='user.User', verbose_name=_('Seller'), related_name='seller',
                                    on_delete=models.CASCADE, null=True, blank=True)
    buyer = models.ForeignKey(to='user.User', verbose_name=_('Buyer'), related_name='buyer',
                                    on_delete=models.CASCADE, null=True, blank=True)
    amount_of_quantities = models.PositiveIntegerField(verbose_name=_('Amount of quantities'), default=0,
                                    null=True, blank=True)
    unit_price = models.DecimalField(verbose_name=_('Unit price'),  max_digits=10, decimal_places=2, null=True, blank=True)
    cost = models.DecimalField(verbose_name=_('Cost'),  max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField( verbose_name=_('status'), max_length=30, choices=STATUS_CHOICE, default=PENDING)