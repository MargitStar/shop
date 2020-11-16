from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
from django.views.generic import UpdateView, TemplateView, DetailView
from django.http import HttpResponseRedirect


class ProfileView(DetailView):
    model = models.Profile
    template_name = 'my_profile/profile_view.html'



