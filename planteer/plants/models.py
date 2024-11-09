from django.db import models


class Plant(models.Model):
    class Category(models.TextChoices):
        FLOWER = 'Flower', 'Flower'
        TREE = 'Tree', 'Tree'
        SHRUB = 'Shrub', 'Shrub'
        VEGETABLE = 'Vegetable', 'Vegetable'
        HERB = 'Herb', 'Herb'

    name = models.CharField(max_length=100)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='plant_images/')
    category = models.CharField(max_length=20, choices=Category.choices)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
