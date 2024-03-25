from django import forms

from wss_app.accounts.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'password']

    password = forms.CharField(
        widget=forms.PasswordInput()
    )
