from django.core.management.base import BaseCommand


# Our command:
#   python manage.py greet <name>
class Command(BaseCommand):
    help = 'Greets the user'
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies User name')
    
    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        greet = f'Hi {name}, Good Morning!'
        self.stdout.write(self.style.SUCCESS(greet))
        self.stdout.write(self.style.WARNING(greet))
        self.stdout.write(self.style.ERROR(greet))
        self.stdout.write(greet)