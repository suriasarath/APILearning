from django.core.management import BaseCommand
import random
from faker import Faker
from serviceone.models import Product,Policy
from django.apps import apps
from django.contrib.auth import get_user_model
import random
User = get_user_model()


class Command(BaseCommand):
    help = "create Fake data"

    def add_arguments(self, parser):
        parser.add_argument('count',type=int, help="Number of fake products")
        parser.add_argument('model',type=str, help="Please select data_name")
        return super().add_arguments(parser)

    def handle(self,*args,**options):
        count =  options['count']
        model_name = options['model']
        fake  = Faker()
        try:
            model = apps.get_model('serviceone',model_name)
            if model_name == "product":
                for _ in range(100):
                    Product.objects.create(
                    name=fake.unique.word().title(),
                    description=fake.text(max_nb_chars=100),
                    insurance_type=random.choice(['vehicle', 'health', 'life', 'property']),
                    premium=round(random.uniform(500, 5000), 2),
                    coverage_amount=round(random.uniform(10000, 100000), 2),
                    duration_months=random.choice([6, 12, 24, 36])
                    )
            elif model_name == "policy":
                users = User.objects.all()
                products = Product.objects.all()
                for _ in range(100):
                    Policy.objects.create(
                        user=random.choice(users),
                        product=random.choice(products),
                        policy_number=fake.unique.bothify(text='POL#####'),
                        start_date=fake.date_between(start_date='-2y', end_date='today'),
                        end_date=fake.date_between(start_date='today', end_date='+2y'),
                        premium_amount=round(random.uniform(500, 5000), 2),
                        coverage_amount=round(random.uniform(10000, 100000), 2),
                        status=random.choice(['active', 'expired', 'pending'])
                    )
            print(f"{model_name} data created successfully")
                
        except Exception as e:
            print(f"{options['model']} Not found {e}")
        for _ in range(count):
            pass

        #super().handle(*args,**options)