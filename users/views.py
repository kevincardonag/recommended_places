from django.views.generic import CreateView
from .models import UserProfile
from .forms import UserProfileForm


class UserCreateView(CreateView):
    form_class = UserProfileForm
    model = UserProfile