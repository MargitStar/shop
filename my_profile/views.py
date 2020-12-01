from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import forms
from . import models
from django.views.generic import UpdateView, TemplateView


class ProfileView(LoginRequiredMixin, TemplateView):
    model = models.Profile
    template_name = 'my_profile/profile_view.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = self.request.user
        profile = models.Profile.objects.filter(user=user).first()

        if user.first_name:
            profile.first_name = user.first_name

        if user.last_name:
            profile.last_name = user.last_name

        profile.email = user.email

        profile.save()

        context['profile'] = profile
        return context


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = models.Profile
    login_url = reverse_lazy('login')
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
