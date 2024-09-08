from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    help = "Insert data into database"
    
    def handle(self, *args, **kwargs):
        # Insert data into database
        dataset = [
            {'roll_num': 1003, 'name': 'Stephan', 'age':153},
            {'roll_num': 1004, 'name': 'Klaus', 'age':1058 },
            {'roll_num': 1009, 'name': 'Maggie', 'age':22},
            {'roll_num': 1010, 'name': 'Apu', 'age':39},
            {'roll_num': 1011, 'name': 'Mike', 'age':19},
            {'roll_num': 1012, 'name': 'Emma', 'age':29},
            {'roll_num': 1013, 'name': 'Bonnie', 'age':17}, 
        ]
        
        for data in dataset:
            roll_num = data['roll_num']
            existing_student = Student.objects.filter(roll_num=roll_num).exists()
            if not existing_student:
                Student.objects.create(**data)
            else:
                self.stdout.write(self.style.ERROR(f"Student with Roll no.:{roll_num} already exists!"))
        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))