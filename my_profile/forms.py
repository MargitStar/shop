from django import forms
from . import models


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = '__all__'


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = '__all__'


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = '__all__'
