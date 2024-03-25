from wss_app.accounts.models import Profile


def get_profile():
    return Profile.objects.first()
