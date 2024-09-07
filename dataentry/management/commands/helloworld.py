from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Prints Hello World!"
    
    def handle(self, *args, **kwargs):
        '''
            This method is called when the command is run.
            It prints "Hello World!" to the console.
        '''
        self.stdout.write("Hello World!")