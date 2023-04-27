from django.core.management.base import BaseCommand
from Attendance.management import initialize_db

class Command(BaseCommand):
    help = "Init scheduler or do some staff in the database."

    def handle(self, *args, **options):
        initialize_db.initialize()
        