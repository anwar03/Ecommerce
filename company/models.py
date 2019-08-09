from django.db import models
from django.utils.translation import ugettext_lazy as _

from base.models import BaseModel
from user.models import User


class Company(BaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=100)
    contact = models.ForeignKey(to='contact.Contact', on_delete=models.SET_NULL, null=True, blank=True)
    address = models.ForeignKey(to='contact.Address', on_delete=models.SET_NULL, null=True, blank=True)
    logo = models.ImageField(verbose_name=_('logo'), upload_to='company/', null=True, blank=True)
    website = models.URLField(verbose_name=_('website'), null=True, blank=True)
    owner = models.ForeignKey(to='User', verbose_name=_('Owner'), related_name='owner', null=True, blank=True)
    
    def __str__(self):
        return self.name
