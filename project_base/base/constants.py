import pytz
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# common timezone from pytz
TIMEZONE_CHOICES = [(t, t) for t in pytz.common_timezones]

PAID, PENDING = 'paid',  'pending'
STATUS_CHOICE = ((PAID, _('Paid')), (PENDING, _('Pending')))

BUYER, SELLER = 'buyer', 'seller'
USER_TYPE = ((BUYER, _('Buyer')), (SELLER, _('Seller')))
