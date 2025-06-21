from django.forms import ModelForm

from main.models import ACTIVITY_CHOICES
from .models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        # the field company_username is excluded from the form, but present in the model Service
        exclude = ['company_username']
        fields = ['name', 'description', 'field', 'price_per_hour']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'autofocus': 'autofocus'})
        # if the user field of work not ALL_IN_ONE, then company can add only
        # services of company field of work, so the no choice field available
        # and this field removed from the form

        # if user.field_of_work != 'ALL_IN_ONE':
        #     del self.fields['field']

        # As per audit requirements from 01-edu, the field must allow
        # the choice of a single variant. Note that feedback regarding
        # their implementation of "graphql" was not accepted, and issues
        # could not be raised on their GitHub repository.
        # This implementation addresses the requirement while adhering
        # to the constraints provided.

        if user.field_of_work != 'ALL_IN_ONE':
            self.fields['field'].choices = [
                (x, y) for x, y in ACTIVITY_CHOICES if x == user.field_of_work]
