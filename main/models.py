from django.db import models
from django.urls import reverse


class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name
	
	@property
	def get_products(self):
		return Product.objects.filter(category__name=self.name)

#class OptionalExtras(models.Model):
#	name = models.CharField(max_length=50)
#	price = models.DecimalField(default=1.99, max_digits=100, decimal_places=2)
#	checkbox = models.BooleanField(default=False)
#
#	def __str__(self):
#		return self.name


class Product(models.Model):
	name = models.CharField(max_length=200)
	short_description = models.TextField(null=True, blank=True)
	long_description = models.TextField(null=True, blank=True)
	price = models.DecimalField(default=4.00, max_digits=100, decimal_places=2)
	slug = models.SlugField(null=False, unique=True)
	image = models.ImageField(upload_to='product_image')
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Category', blank=True)
	


	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse("product_detail", kwargs={"slug": self.slug})
	
	

class BasketItem(models.Model):
	basket = models.ForeignKey('Basket', null=True, blank=True, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	line_total = models.DecimalField(default=9.99, max_digits=10000, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		try:
			return str(self.basket.id)
		except:
			return self.product.title

class Basket(models.Model):
	total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return "Basket id: %s" %(self.id)

