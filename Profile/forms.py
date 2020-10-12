from django.forms import ModelForm
from .models import Person


class update_person_form(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'bio', 'email', 'profile_pic']
