import os
import django
import random
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth.models import User
from myapp.models import Product

def create_admin_user():
    username = 'abrar'
    email = 'abrar@example.com'
    password = 'Wellcom3$'
    
    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser '{username}'...")
        User.objects.create_superuser(username, email, password)
        print("Superuser created.")
    else:
        print(f"Superuser '{username}' already exists.")

def create_products():
    products_data = [
        {
            "name": "Wireless Noise-Canceling Headphones",
            "description": "Experience crystal-clear sound with our premium wireless headphones. Features active noise cancellation and 30-hour battery life.",
            "price": "299.99",
            "stock": 50
        },
        {
            "name": "Smart Fitness Watch",
            "description": "Track your health and fitness goals with this advanced smartwatch. Monitors heart rate, sleep, and activity levels.",
            "price": "149.50",
            "stock": 100
        },
        {
            "name": "4K Ultra HD Action Camera",
            "description": "Capture your adventures in stunning 4K resolution. Waterproof, durable, and comes with a variety of mounts.",
            "price": "199.00",
            "stock": 30
        },
        {
            "name": "Mechanical Gaming Keyboard",
            "description": "Dominate your games with this high-performance mechanical keyboard. customizable RGB lighting and tactile switches.",
            "price": "89.99",
            "stock": 75
        },
        {
            "name": "Portable Bluetooth Speaker",
            "description": "Bring the party wherever you go. Powerful bass, waterproof design, and 12 hours of playtime.",
            "price": "59.95",
            "stock": 120
        },
        {
            "name": "Ergonomic Office Chair",
            "description": "Work in comfort with this fully adjustable office chair. Lumbar support, breathable mesh, and smooth-rolling casters.",
            "price": "249.00",
            "stock": 20
        }
    ]

    print("Seeding products...")
    for data in products_data:
        product, created = Product.objects.get_or_create(
            name=data['name'],
            defaults={
                'description': data['description'],
                'price': Decimal(data['price']),
                'stock': data['stock']
            }
        )
        if created:
            print(f"Created product: {product.name}")
        else:
            print(f"Product already exists: {product.name}")

if __name__ == '__main__':
    create_admin_user()
    create_products()
    print("Database seeding completed.")
