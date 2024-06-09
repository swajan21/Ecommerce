from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


STATE_CHOICES=(
    ('Dhaka','Dhaka'),
    ('Tangail','Tangail'),
    ('Gazipur','Gazipur'),
    ('Faridpur','Faridpur'),
    ('Gopalganj','Gopalganj'),
    ('Jamalpur','Jamalpur'),
    ('Kishoreganj','Kishoreganj'),
    ('Madaripur','Madaripur'),
    ('Manikganj','Manikganj'),
    ('Munshiganj','Munshiganj'),
    ('Mymensingh','Mymensingh'),
    ('Narayanganj','Narayanganj'),
    ('Narsingdi','Narsingdi'),
    ('Netrokona','Netrokona'),
    ('Rajbari','Rajbari'),
    ('Shariatpur','Shariatpur'),
    ('Sherpur','Sherpur'),
    ('Bogra','Bogra'),
    ('Joypurhat','Joypurhat'),
    ('Naogaon','Naogaon'),
    ('Natore','Natore'),
    ('Nawabganj','Nawabganj'),
    ('Pabna','Pabna'),
    ('Rajshahi','Rajshahi'),
    ('Sirajgonj','Sirajgonj'),
    ('Dinajpur','Dinajpur'),
    ('Gaibandha','Gaibandha'),
    ('Kurigram','Kurigram'),
    ('Lalmonirhat','Lalmonirhat'),
    ('Nilphamari','Nilphamari'),
    ('Panchagarh','Panchagarh'),
    ('Rangpur','Rangpur'),
    ('Thakurgaon','Thakurgaon'),
    ('Barguna','Barguna'),
    ('Barisal','Barisal'),
    ('Bhola','Bhola'),
    ('Jhalokati','Jhalokati'),
    ('Patuakhali','Patuakhali'),
    ('Pirojpur','Pirojpur'),
    ('Bandarban','Bandarban'),
    ('Brahmanbaria','Brahmanbaria'),
    ('Chandpur','Chandpur'),
    ('Chittagong','Chittagong'),
    ('Comilla','Comilla'),
    ('Cox''s Bazar','Cox''s Bazar'),
    ('Feni','Feni'),
    ('Khagrachari','Khagrachari'),
    ('Lakshmipur','Lakshmipur'),
    ('Noakhali','Noakhali'),
    ('Rangamati','Rangamati'),
    ('Habiganj','Habiganj'),
    ('Maulvibazar','Maulvibazar'),
    ('Sunamganj','Sunamganj'),
    ('Sylhet','Sylhet'),
    ('Bagerhat','Bagerhat'),
    ('Chuadanga','Chuadanga'),
    ('Jessore','Jessore'),
    ('Jhenaidah','Jhenaidah'),
    ('Khulna','Khulna'),
    ('Kushtia','Kushtia'),
    ('Magura','Magura'),
    ('Meherpur','Meherpur'),
    ('Narail','Narail'),
    ('Satkhira','Satkhira'),
)


CATEGORY_CHOICES=(
    ('LA','Laptop'),
    ('MO','Mobile'),
    ('SO','Soundbox'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    brand = models.CharField(max_length=100)
    stock = models.IntegerField()
    product_image = models.ImageField(upload_to='product') 
    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.discounted_price
    
    
 
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    district = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return str(self.id)
    

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price   


STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)  



class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='Pending')
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price 



class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price



class Slider(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='slider')
    image = models.ImageField(upload_to='slider')
    is_active = models.BooleanField(default=False)
    descriptions = models.TextField()
    brand_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.title
    


class Information(models.Model):
    information = models.TextField()

    def __str__(self):
        return self.information

    