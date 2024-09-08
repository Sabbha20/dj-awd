from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    help = "Insert data into database"
    
    def handle(self, *args, **kwargs):
        # Insert data into database
        dataset = [
            {'roll_num': 1003, 'name': 'Stephan', 'age':153},
            {'roll_num': 1004, 'name': 'Klaus', 'age':1058 },
            {'roll_num': 1005, 'name': 'Bart', 'age':43},
            {'roll_num': 1006, 'name': 'Lisa', 'age':36},
            {'roll_num': 1007, 'name': 'Homer', 'age':45},
            {'roll_num': 1008, 'name': 'Marge', 'age':38},
            {'roll_num': 1009, 'name': 'Maggie', 'age':22},
            {'roll_num': 1010, 'name': 'Apu', 'age':39},
        ]
        
        for data in dataset:
            Student.objects.create(**data)
        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))