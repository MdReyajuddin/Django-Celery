import string

from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from celery import shared_task


@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(get_random_string(username))
        password = '{}'.format(get_random_string(50))
        User.objects.create_user(username=username, password=password, email=email)
        return '{} record successfully created!'.format(total)