from django.core.management.base import BaseCommand, CommandError
# from dataentry.models import Student
from django.apps import apps # Importing all apps
import csv

# Proposed command - python manage.py importdata <file_path> <model_name>

class Command(BaseCommand):
    help = 'Import data from CSV file'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to CSV file")
        parser.add_argument('model_name', type=str, help="Name of the model")
        
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()
        
        # Search for the models accross all apps
        model = None
        for app_config in apps.get_app_configs():
            # print(app_config)
            # for model_name in app_config.get_models():
            #     print("  - ",model_name)
            try:
                model = apps.get_model(app_config.label, model_name)
                break # Once we get model, will stop searching for it
            except LookupError:
                continue # Will continue, till we get our model
            
        if not model:
            raise CommandError(f"Model: {model_name} not found in any apps!")
        
        try:
            with  open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    model.objects.create(**row)
                    # print(row)
            self.stdout.write(self.style.SUCCESS("Data imported successfully!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR("'File Path' & 'Model name' mismatch!!!"))