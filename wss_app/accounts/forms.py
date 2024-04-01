from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class WssUserCreationForm(auth_forms.UserCreationForm):
    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class WssChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
