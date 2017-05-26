from django import forms
from users.models import UserProfile
from django.utils.translation import ugettext_lazy as _


class SignupForm(forms.Form):
    """
    Autor: Kevin Cardona
    Fecha: clase que representa el formulario de crear usuario.Propia de django all-auth
    """
    first_name = forms.CharField(max_length=30, label=_('Nombres'))
    last_name = forms.CharField(max_length=30, label=_('Apellidos'))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class UserProfileForm(forms.ModelForm):

    required_css_class = 'required'

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'photo', 'email']
