import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()
topics = [ 'New', 'Normal', 'Premium' ]

# def add_topic():
#     t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t

def populate(N=5):
    for entry in range(N):
        # top = add_topic()

        fake_name = fakegen.name().split()
        fake_first = fake_name[0]
        fake_last = fake_name[1]

        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name = fake_first, last_name = fake_last, email=fake_email)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete!')
