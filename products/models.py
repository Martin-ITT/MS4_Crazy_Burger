from django.db import models


class Category(models.Model):
    # Change plural name in admin page
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Allergen(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    # sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    allergens = models.ManyToManyField(Allergen, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # size to be displayed on pages - small, 0.33l...
    size = models.CharField(max_length=10, default='small')
    # price for medium and large if available for some categories
    has_sizes = models.BooleanField(default=False)
    price_medium = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.0)
    size_medium = models.CharField(max_length=10, default='medium')
    price_large = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.0)
    size_large = models.CharField(max_length=10, default='large')
    # to upgrade to a meal option
    price_meal = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.0)
    has_toppings = models.BooleanField(default=False)
    price_topping_medium = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    price_topping_large = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    toppings = models.ManyToManyField(Topping, blank=True)
    # rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    # image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
