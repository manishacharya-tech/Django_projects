import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geeks_site.settings')
import django
django.setup()

from faker import Faker as Fk
import random
from first_app.models import User_name
fake = Fk()
django.setup()
# topic = ['Social', 'Search','MarketPlace','Games','News']

# def add_topic():
#     t = Topic.objects.get_or_create(top_name=random.choice(topic))[0]
#     t.save()
#     return t

def populate(N):
    for _ in range(N):
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()
        user = User_name.objects.get_or_create(email=email, first_name=first_name, last_name=last_name)[0]
        user.save()

if __name__ == '__main__':
    print('Starting')
    populate(20)
    print('Finished')