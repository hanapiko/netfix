from django.contrib.auth.backends import BaseBackend
from main.models import AppUser

class EmailBackend(BaseBackend):
    """allows to make authentication with email instead of username.
    The "request" and "kwargs" are not used, but they are required to implement
    additional functionality(of common case), and remove them is not a safe stuff
    """

    def authenticate(self, request=None, email=None, password=None, **kwargs):
        try:
            # check if the email is registered
            user = AppUser.objects.get(email=email)
        except AppUser.DoesNotExist:
            return None

        # check the password of user is the same as incoming password.
        # the password will be automatically encrypted by django, before comparing
        if password is not None and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return AppUser.objects.get(pk=user_id)
        except AppUser.DoesNotExist:
            return None
