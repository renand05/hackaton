import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inventory.settings")
django.setup()

from app.models import Provider, Product, Customer, Stock, Order, Point
from faker import Faker

fakegen = Faker()

def add_data(N):
    for _ in range(N):
        name = fakegen.company()
        expiration_date = fakegen.date_time()
        provider = Provider.objects.create(name=name, expiration_date=expiration_date)
        for _ in range(N):
            name = fakegen.word()
            expiration_date = fakegen.date_time()
            price = fakegen.pyfloat(positive=True)
            points = fakegen.pyint()
            ratio = fakegen.pyint()
            active = 1
            product = Product.objects.create(name=name, expiration_date=expiration_date, price=price, points=points, ratio=ratio, active=active, provider=provider)
            qty = fakegen.pyint()
            Stock.objects.create(quantity=qty, product=product)
            
    for _ in range(N):
        name = fakegen.name()
        email = fakegen.company_email()
        customer = Customer.objects.create(name=name, email=email)
        for _ in range(N):
            product = Product.objects.order_by('?').first()
            quantity = fakegen.pyint()
            status = 0
            Order.objects.create(customer=customer, product=product, quantity=quantity, status=status)

            quantity = fakegen.pyint()
            expiration_date = fakegen.date_time()
            Point.objects.create(customer=customer, quantity=quantity, expiration_date=expiration_date)


def populate():
    Order.objects.all().delete()
    Stock.objects.all().delete()
    Product.objects.all().delete()
    Point.objects.all().delete()
    Customer.objects.all().delete()
    Provider.objects.all().delete()
    add_data(10)

populate()
print('Data is populated successfully')
