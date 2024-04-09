from django import forms

from wss_app.user_interaction.models import ContactMessage, Review


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['subject', 'message']

    widgets = {
        "subject": forms.EmailInput(attrs={"placeholder": "Please enter subject", 'required': True}),
        "message": forms.Textarea(attrs={"placeholder": "Enter your message", 'required': True}),
    }
    labels = {
        "subject": "Subject",
        "message": "Message",
    }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
