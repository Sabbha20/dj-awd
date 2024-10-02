import csv
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps

import datetime

# Proposed Command - python manage.py exportdata <model_name>
class Command(BaseCommand):
    help = "Export data from database to CSV file"
    
    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help="Name of the model")
    
    def handle(self, *args, **kwargs):
        ts = datetime.datetime.now().strftime('%d%b%Y_%H%M%S')
        model_name = kwargs['model_name'].capitalize()
        
        file_path = f'exported_{model_name}_data_{ts}.csv'
        # print(file_path)
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
        
        # fetch data  from database
        data = model.objects.all()
        
        # print([field.name for field in model._meta.fields])
        
        # open csv to write
        try:
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                
                # writing the headers
                writer.writerow([field.name for field in model._meta.fields])
                
                for dt in data:
                    writer.writerow([getattr(dt, field.name) for field in model._meta.fields])
            self.stdout.write(self.style.SUCCESS("Data exported successfully!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Export Error:{e}"))
        
        
        
        
        
    