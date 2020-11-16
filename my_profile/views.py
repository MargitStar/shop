from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
from django.views.generic import UpdateView, TemplateView, DetailView
from django.http import HttpResponseRedirect


class ProfileView(TemplateView):
    model = models.Profile
    template_name = 'my_profile/profile_view.html'


class UpdateProfileView(UpdateView):
    model = models.Profile
    template_name = 'my_profile/update_profile.html'
    fields = ('first_name',
              'last_name',
              'email',
              'phone_number',
              'country',
              'city',
              'address1',
              'address2',
              'zip_code',
              'additional_info')
    success_url = '/profile'
