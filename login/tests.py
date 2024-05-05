from django.contrib.auth.models import User

default_username = 'user'
default_password = 'password'

if not User.objects.filter(username=default_username).exists():
    user = User.objects.create_user(username=default_username, password=default_password)
    user.email = 'default@example.com'
    user.first_name = 'Default'
    user.last_name = 'User'
    user.save()
    print(f'Default user created: {default_username}')
else:
    print(f'User {default_username} already exists.')