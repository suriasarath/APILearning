from serviceone.models import Product
from faker import Faker
import random

fake = Faker()

for _ in range(200):
    Product.objects.create(
        name=fake.unique.word().title(),
        description=fake.text(max_nb_chars=100),
        insurance_type=random.choice(['vehicle', 'health', 'life', 'property']),
        premium=round(random.uniform(500, 5000), 2),
        coverage_amount=round(random.uniform(10000, 100000), 2),
        duration_months=random.choice([6, 12, 24, 36])
    )
print("200 fake products created.")
 