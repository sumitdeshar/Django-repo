import os
import django
from faker import Faker
from myapp.models import Features, AllowedIP

fake = Faker()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

def seed_data():
   
    for _ in range(10):  
        Features.objects.create(
            name=fake.word(),  # Use appropriate Faker method for your data
            details=fake.text(),  # Use appropriate Faker method for your data
        )

    for _ in range(5): 
        AllowedIP.objects.create(
            ip_address=fake.ipv4()  # Use appropriate Faker method for your data
        )

seed_data()

