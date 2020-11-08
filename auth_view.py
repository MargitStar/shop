from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin


class MyLogInView(LoginView):
    template_name = 'registration/log_in.html'
    success_url = '/'


class MyLogOutView(LogoutView):
    template_name = 'registration/log-out.html'


class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = '/password_change_done'


class MyPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'
