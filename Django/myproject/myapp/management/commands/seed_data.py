# your_app/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from myapp.seeder import seed_data  # Import your seeder function

class Command(BaseCommand):
    help = 'Seeds data for your models'

    def handle(self, *args, **options):
        seed_data()
        self.stdout.write(self.style.SUCCESS('Data seeding complete.'))
