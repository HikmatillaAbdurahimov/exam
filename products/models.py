from django.db import models

""" bu classda yano tablda tur (misol==>poliz ekinlari)   """
class Categories(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=250)
    image=models.ImageField(upload_to='products/turi')
    description=models.TextField()
    count=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
""" bu classda esa nomlari (misol==>sabzi bu ==> poliz ekinlari) """
class Products(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=250)
    descriptions=models.TextField()
    product_type = models.ManyToManyField(Categories)
    image=models.ImageField(upload_to='products/nomi')
    price=models.FloatField(default=0)
    count=models.PositiveIntegerField(default=0)
    rating=models.FloatField(default=0)

    def __str__(self):
        return f"{self.title}"


