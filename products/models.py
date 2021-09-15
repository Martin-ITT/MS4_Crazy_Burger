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
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    allergens = models.ManyToManyField(Allergen, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # to upgrade burger for a meal
    price_meal = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # milkshakes, drinks and some other dishes
    price_medium = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    price_large = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    has_toppings = models.BooleanField(initial=False)
    toppings = models.ManyToManyField(Topping, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
