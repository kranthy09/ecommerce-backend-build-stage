"""
Populates Database
"""

import random
from django.core.management.base import BaseCommand
from core.models import Product, Category


class Command(BaseCommand):
    """
    Populates the database with dummy data.
    """

    help = "Populates the database with dummy data"

    def handle(self, *args, **kwargs):
        """handles model creation functions"""
        Product.objects.all().delete()
        Category.objects.all().delete()
        categories = self.create_categorys()
        self.create_products(categories)
        self.stdout.write(
            "Successfully populated the database with dummy data."
        )

    def create_categorys(self, *args, **kwargs):
        """creates dummy categories"""
        categories = [
            Category(
                name=f"Category {i}", description=f"Category Description {i}"
            )
            for i in range(5)
        ]
        Category.objects.bulk_create(categories)
        self.stdout.write("Successfully created dummy categories.")
        return categories

    def create_products(self, *args, **kwargs):
        """creates dummy products"""
        categories = Category.objects.all()
        image_urls = [
            f"https://picsum.photos/seed/{random.randint(1, 1000)}/300/200"
            for _ in range(100)
        ]
        products = [
            Product(
                name=f"Product {i}",
                description=f"Product Description {i}",
                price=random.randint(1, 100),
                stock=random.randint(1, 100),
                image_url=random.choice(image_urls),
                category=random.choice(categories),
            )
            for i in range(40)
        ]
        Product.objects.bulk_create(products)
        self.stdout.write("Successfully created dummy products.")
