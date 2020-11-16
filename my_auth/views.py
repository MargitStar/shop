from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect


class MyLogInView(LoginView):
    template_name = 'registration/log_in.html'
    success_url = 'profile/'


class MyLogOutView(LogoutView):
    template_name = 'registration/log-out.html'


class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = '/password_change_done'


class MyPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'


class SignUpView(CreateView):
    template_name = 'registration/sign-up.html'
    success_url = '/'
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect('/')

