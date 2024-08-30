from django.core.management.base import BaseCommand
from master.models import Status

class Command(BaseCommand):
    help = 'Populate status table with default statuses'

    def handle(self, *args, **kwargs):
        statuses = [
            {'name': 'Active', 'description': 'Item is active and available'},
            {'name': 'Inactive', 'description': 'Item is inactive and not available'},
            {'name': 'Pending', 'description': 'Item is pending approval'},
            {'name': 'Archived', 'description': 'Item is archived and not active'}
        ]

        for status_data in statuses:
            status, created = Status.objects.get_or_create(name=status_data['name'], defaults=status_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created status: {status.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Status already exists: {status.name}"))
