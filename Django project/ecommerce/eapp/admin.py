from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import *


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','district']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','description','category','brand','stock','product_image',]


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','customer_info','product_info','product','quantity','ordered_date','status'] 

    def customer_info(self, obj):
        link = reverse("admin:eapp_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)
    
    def product_info(self, obj):
        link = reverse("admin:eapp_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product']


@admin.register(Slider)
class  SliderModelAdmin(admin.ModelAdmin):
    list_display = ['id','product','image','is_active','created']


@admin.register(Information)
class  InformationModelAdmin(admin.ModelAdmin):
    list_display = ['id','information']


