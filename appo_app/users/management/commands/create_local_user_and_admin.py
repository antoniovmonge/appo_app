from allauth.account.models import EmailAddress
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Create the basic superuser
    `docker-compose -f local.yml run --rm django python manage.py create_local_user_and_admin`
    """

    def handle(self, *args, **options):

        User = get_user_model()

        # username = options["user"]
        email = "admin@email.com"
        password = "testpass123"

        if settings.DEBUG:
            """SuperUser"""
            if User.objects.filter(email="admin@email.com").exists():
                print("The admin user already exists.")
            else:
                User.objects.create_superuser(email=email, password=password)
                EmailAddress.objects.create(
                    # User is selected in this way because it must be a MaterialsUser Instance
                    user=User.objects.get(email="admin@email.com"),
                    email="admin@email.com",
                    verified=True,
                    primary=True,
                )
                self.stdout.write('Local superuser "admin" was created')
            """Local Normal User"""
            if User.objects.filter(email="user@email.com").exists():
                print("The local default user already exists.")
            else:
                User.objects.create_user(email="user@email.com", password=password)
                EmailAddress.objects.create(
                    # User is selected in this way because it must be a MaterialsUser Instance
                    user=User.objects.get(email="user@email.com"),
                    email="user@email.com",
                    verified=True,
                    primary=True,
                )
                self.stdout.write('Local local user "user" was created')

        else:
            print("Sorry, this command can be only executed when running locally.")
