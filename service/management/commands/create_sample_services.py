from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from service.models import Service
from decimal import Decimal

User = get_user_model()


class Command(BaseCommand):
    help = 'Create sample services for testing and development'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing services before creating new ones',
        )

    def handle(self, *args, **options):
        if options['clear']:
            Service.objects.all().delete()
            self.stdout.write(
                self.style.WARNING('Cleared all existing services')
            )

        # sample company users 
        sample_companies = [
            {
                'username': 'quickfix_plumbing',
                'email': 'quickfixplumbing@gmail.com',
                'field_of_work': 'PLUMBING',
                'first_name': 'Quick',
                'last_name': 'Fix Plumbing'
            },
            {
                'username': 'sparkle_electric',
                'email': 'sparkleelectric@gmail.com',
                'field_of_work': 'ELECTRICITY',
                'first_name': 'Sparkle',
                'last_name': 'Electric'
            }
        ]

        # sample customer users
        sample_customers = [
            {
                'username': 'john_customer',
                'email': 'johndoe@gmail.com',
                'field_of_work': 'CUSTOMER',
                'first_name': 'John',
                'last_name': 'Doe'
            },
            {
                'username': 'mary_customer',
                'email': 'marysmith@gmail.com',
                'field_of_work': 'CUSTOMER',
                'first_name': 'Mary',
                'last_name': 'Smith'
            }
        ]

        # Combine all users
        all_users = sample_companies + sample_customers

        created_users = []
        for user_data in all_users:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'field_of_work': user_data['field_of_work'],
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name'],
                    'date_of_birth': '1990-01-01'
                }
            )
            if created:
                user.set_password('defaultpass123')
                user.save()
                user_type = "company" if user_data['field_of_work'] != 'CUSTOMER' else "customer"
                self.stdout.write(f'Created {user_type} user: {user.username}')
            created_users.append(user)

        # Sample services data
        sample_services = [
            {
                'name': 'Emergency Pipe Repair',
                'description': 'Quick and reliable emergency pipe repair service available 24/7. We handle burst pipes, leaks, and blockages with professional equipment.',
                'field': 'PLUMBING',
                'price_per_hour': Decimal('45.00'),
                'company_username': 'quickfix_plumbing'
            },
            {
                'name': 'Home Electrical Wiring',
                'description': 'Professional electrical wiring services for new homes and renovations. Licensed electricians with 10+ years experience.',
                'field': 'ELECTRICITY',
                'price_per_hour': Decimal('60.00'),
                'company_username': 'sparkle_electric'
            },
            {
                'name': 'Ceiling Fan Installation',
                'description': 'Expert ceiling fan installation and repair services. We handle all brands and models with warranty included.',
                'field': 'ELECTRICITY',
                'price_per_hour': Decimal('40.00'),
                'company_username': 'sparkle_electric'
            }
        ]

        created_services = 0
        for service_data in sample_services:
            try:
                company_user = User.objects.get(username=service_data['company_username'])
                service, created = Service.objects.get_or_create(
                    name=service_data['name'],
                    company_username=company_user,
                    defaults={
                        'description': service_data['description'],
                        'field': service_data['field'],
                        'price_per_hour': service_data['price_per_hour']
                    }
                )
                if created:
                    created_services += 1
                    self.stdout.write(f'Created service: {service.name}')
                else:
                    self.stdout.write(f'Service already exists: {service.name}')
            except User.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'Company user {service_data["company_username"]} not found')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_services} new services')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Total services in database: {Service.objects.count()}')
        )
