import os

# key = os.environ['DJANGO_SECRET_KEY']
key = os.environ.get('DJANGO_SECRET_KEY')

print(key)