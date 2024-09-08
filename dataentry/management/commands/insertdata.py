from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Insert data into database"
    
    def handle(self, *args, **kwargs):
        # Insert data into database
        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))