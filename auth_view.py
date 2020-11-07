from django.contrib.auth.views import LoginView


class MyLogInView(LoginView):
    template_name = 'registration/log_in.html'
