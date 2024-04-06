from django import forms

from wss_app.user_interaction.models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['email', 'message']

    widgets = {
        "email": forms.EmailInput(attrs={"placeholder": "Please enter email", 'required': True}),
        "message": forms.Textarea(attrs={"placeholder": "Enter your message", 'required': True}),
    }
    labels = {
        "email": "Email",
        "message": "Message",
    }