import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

username = "vinay"
email = "vinay@gmail.com"
password = "123"

try:
    user = User.objects.get(username=username)
    user.email = email
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print(f"Updated password and permissions for subperuser '{username}'")
except User.DoesNotExist:
    User.objects.create_superuser(username, email, password)
    print(f"Created superuser '{username}'")
