from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    help = "Insert data into database"
    
    def handle(self, *args, **kwargs):
        # Insert data into database
        dataset = [
            {'roll_num': 1001, 'name': 'Sabbha Mondal', 'age':10053},
            {'roll_num': 1002, 'name': 'Andrea Marshall', 'age':273},
            {'roll_num': 1003, 'name': 'Stephan Salvatore', 'age':153},
            {'roll_num': 1004, 'name': 'NiKlaus Micheleson', 'age':1058 },
            {'roll_num': 1005, 'name': 'Damon Salvatore', 'age':163},
            {'roll_num': 1006, 'name': 'Elaiza Micheleson', 'age':1068 },
            {'roll_num': 1007, 'name': 'Ribekka Micheleson', 'age':1018 },
            {'roll_num': 1008, 'name': 'Jerr Gilbert', 'age':22},
            {'roll_num': 1009, 'name': 'Maggie Robert', 'age':22},
            {'roll_num': 1010, 'name': 'Apu Ghar', 'age':39},
            {'roll_num': 1011, 'name': 'Mike Tyson', 'age':19},
            {'roll_num': 1012, 'name': 'Emma Bennet', 'age':29},
            {'roll_num': 1013, 'name': 'Bonnie Lawrence', 'age':17}, 
        ]
        
        for data in dataset:
            roll_num = data['roll_num']
            existing_student = Student.objects.filter(roll_num=roll_num).exists()
            if not existing_student:
                Student.objects.create(**data)
            else:
                self.stdout.write(self.style.ERROR(f"Student with Roll no.:{roll_num} already exists!"))
        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))