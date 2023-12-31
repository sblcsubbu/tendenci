from django.db.models import Q
from django.template import Library

from tendenci.apps.invoices.models import Invoice


register = Library()


@register.filter
def allow_edit_by(profile, user):
    """
    Check if the profile allows to be edited by the user. Returns True/False.
    """
    return profile.allow_edit_by(user)


@register.filter
def invoice_count(user):
    inv_count = Invoice.objects.filter(Q(creator=user) | Q(owner=user) | Q(bill_to_email=user.email)).count()

    return inv_count


@register.filter
def get_ud_field(profile, ud):
    """
    Get the value for the ud field
    """
    from tendenci.apps.profiles.models import Profile
    if isinstance(profile, Profile):
        if hasattr(profile, 'user'):
            if hasattr(profile.user, 'demographics'):
                demographics = profile.user.demographics
                if demographics:
                    return getattr(demographics, ud, '')
    return ''