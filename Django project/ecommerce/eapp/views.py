from django.shortcuts import render,redirect
from django.views import View
from .forms import CustomerRegistration,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *




class ProductView(View):
    def get(self, request):
        totalitem = 0
        wishitem = 0
        infor = Information.objects.get(id=1)
        sliders = Slider.objects.filter(is_active=True)
        laptop = Product.objects.filter(category = 'LA')
        mobile = Product.objects.filter(category = 'MO')
        soundbox = Product.objects.filter(category = 'SO')
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        
        context={
            'laptop':laptop,
            'mobile':mobile,
            'soundbox':soundbox,
            'totalitem':totalitem,
            'wishitem':wishitem,
            'infor':infor,
            'sliders':sliders,
            
        }

        return render(request, "app/home.html",context)
        
@login_required
def About(request):
    totalitem = 0
    wishitem = 0
    infor = Information.objects.get(id=2)
    sliders = Slider.objects.filter(is_active=True)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/about.html",{'totalitem':totalitem,'wishitem':wishitem,'sliders':sliders,'infor':infor})

@login_required
def Contact(request):
    totalitem = 0
    wishitem = 0
    infor = Information.objects.get(id=3)
    sliders = Slider.objects.filter(is_active=True)
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/contact.html",{'totalitem':totalitem,'wishitem':wishitem,'sliders':sliders,'infor':infor})


class ProductDetail(View):
    def get(self,request,pk):
        totalitem = 0
        wishitem = 0
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        item_already_in_wishlist = False
        if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))
         wishitem = len(Wishlist.objects.filter(user=request.user))
         item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
         item_already_in_wishlist = Wishlist.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, "app/productdetail.html",{'product':product,'item_already_in_cart':item_already_in_cart,'totalitem':totalitem,'wishitem':wishitem,'item_already_in_wishlist':item_already_in_wishlist})
    

def mobile(request, data=None):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    if data == None:
        mobiles = Product.objects.filter(category= 'MO')
    elif data == 'Samsung' or data == 'Redmi' or data == 'Infinix' or data == 'Xiaomi'or data == 'Itel' or data == 'Tecno' or data == 'Vivo':
        mobiles = Product.objects.filter(category= 'MO').filter(brand=data)
    return render(request, 'app/mobile.html', {'mobiles':mobiles,'totalitem':totalitem,'wishitem':wishitem})   


def laptop(request, data=None):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    if data == None:
        laptops = Product.objects.filter(category= 'LA')
    elif data == 'Asus' or data == 'Lenavo' or data == 'Dell':
        laptops = Product.objects.filter(category= 'LA').filter(brand=data)
    return render(request, 'app/laptop.html', {'laptops':laptops,'totalitem':totalitem,'wishitem':wishitem})  


def soundbox(request, data=None):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    if data == None:
        soundboxs = Product.objects.filter(category= 'SO')
    elif data == 'JBL' or data == 'Lenavo' or data == 'Microlab':
        soundboxs = Product.objects.filter(category= 'SO').filter(brand=data)
    return render(request, 'app/soundbox.html', {'soundboxs':soundboxs,'totalitem':totalitem,'wishitem':wishitem})    

    

class Registration(View):
    def get(self,request):
        form = CustomerRegistration()
        return render(request, 'app/registration.html',locals())
    def post(self,request):
        form = CustomerRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Register Successful")
        else:
            messages.warning(request,"Invalid Input Data !!!")
        return render(request, 'app/registration.html',locals())
    

@method_decorator(login_required, name='dispatch')
class ProfileView(View):    
    def get(self,request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
         totalitem = len(Cart.objects.filter(user=request.user))
         wishitem = len(Wishlist.objects.filter(user=request.user)) 
         form = CustomerProfileForm()
         return render(request, 'app/profile.html',{'form':form,'totalitem':totalitem,'wishitem':wishitem})    
    def post(self,request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
          wishitem = len(Wishlist.objects.filter(user=request.user))
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            district = form.cleaned_data['district']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user,name=name,locality=locality,city=city,district=district,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulation! Profile Save Successfully")
            return redirect("/address")
        else:
            messages.warning(request,"Invalid Input Data")    
        return render(request, 'app/profile.html',{'form':form,'totalitem':totalitem,'wishitem':wishitem}) 

@login_required
def Address(request):
    totalitem = 0
    wishitem = 0

    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user)) 
    add = Customer.objects.filter(user=request.user) 
    return render(request, 'app/address.html',{'add':add,'totalitem':totalitem,'wishitem':wishitem})


def delete_address(request, pk):
    add = Customer.objects.filter(id=pk)
    add.delete()
    messages.success(request, 'Address delete Successfully')
    return redirect("/address")

@login_required
def orders(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user)) 
    op = OrderPlaced.objects.filter(user=request.user) 
    return render(request, 'app/orders.html', {'order_placed':op, 'totalitem':totalitem,'wishitem':wishitem})     


@method_decorator(login_required, name='dispatch')
class Updateaddress(View):
    def get(self,request,pk):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
          wishitem = len(Wishlist.objects.filter(user=request.user))
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'app/updateaddress.html',{'form':form,'totalitem':totalitem,'wishitem':wishitem}) 
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.district = form.cleaned_data['district']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Congratulation! Profile Save Successfully")
        else:
            messages.warning(request,"Invalid Input Data")    
        return redirect("address") 
    

@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect("/cart")




@login_required
def show_cart(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
      totalitem = len(Cart.objects.filter(user=request.user))
      wishitem = len(Wishlist.objects.filter(user=request.user))
      user = request.user
      cart = Cart.objects.filter(user=user)
      amount = 0
      shipping_amount = 50
      totalamount = 0
      cart_product = [p for p in Cart.objects.all() if p.user == user]
      if cart_product:
         for p in cart_product:
             tempamount = (p.quantity * p.product.discounted_price)
             amount = amount + tempamount
             totalamount = amount + shipping_amount
         return render(request, 'app/addtocart.html',{'carts':cart,'totalamount':totalamount, 'amount':amount,'totalitem':totalitem,'wishitem':wishitem})
      else:
        return render(request, 'app/emptycart.html',{'totalitem':totalitem,'wishitem':wishitem})
            
      

@method_decorator(login_required, name='dispatch')
class Checkout(View):
    def get(self,request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
          wishitem = len(Wishlist.objects.filter(user=request.user))
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        amount = 0
        shipping_amount = 50
        totalamount = 0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product:
            for p in cart_product:
              tempamount = (p.quantity * p.product.discounted_price)
              amount = amount + tempamount
            totalamount = amount + shipping_amount 

        return render(request, 'app/checkout.html', {'add':add,'totalamount':totalamount,'cart_items':cart_items,'totalitem':totalitem,'wishitem':wishitem,})
    


@method_decorator(login_required, name='dispatch')
class Checkout2(View):
    def get(self,request,pk):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
          wishitem = len(Wishlist.objects.filter(user=request.user))
        user=request.user
        add=Customer.objects.filter(user=user)
        product = Product.objects.get(pk=pk)
        totalitem = 0
        wishitem = 0
        amount = 0
        shipping_amount = 50
        totalamount = 0
        #buy_product = [p for p in product.objects.all()]
         #if buy_product:
        tempamount = product.discounted_price 
        amount = amount + tempamount
        totalamount = amount + shipping_amount 

        return render(request, 'app/checkout2.html', {'add':add,'totalamount':totalamount,'product':product,'totalitem':totalitem,'wishitem':wishitem,})
    


@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")

@login_required
def payment_done2(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    OrderPlaced(user=user,product=product,customer=customer).save()
    return redirect("orders")



       

        


def plus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0
        shipping_amount = 50
        total_amount = 0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
           tempamount = (p.quantity * p.product.discounted_price)
           amount = amount + tempamount
           
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount + shipping_amount
            } 
        return JsonResponse(data)


    
def minus_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0
        shipping_amount = 50
        total_amount = 0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
           tempamount = (p.quantity * p.product.discounted_price)
           amount = amount + tempamount
           
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount + shipping_amount
        } 
        return JsonResponse(data)  
    


def remove_cart(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0
        shipping_amount = 50
        total_amount = 0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
           tempamount = (p.quantity * p.product.discounted_price)
           amount = amount + tempamount
           
        data={
            'amount':amount,
            'totalamount':amount + shipping_amount
        } 
        return JsonResponse(data) 


#def remove_wishlist(request):
#    if request.method == 'GET':
#        prod_id=request.GET['prod_id']
#        w = Wishlist.objects.get(Q(product=prod_id) & Q(user=request.user))
#        w.delete()
#        amount = 0
#        shipping_amount = 50
#        total_amount = 0
#        cart_product = [p for p in Wishlist.objects.all() if p.user == request.user]
#        for p in cart_product:
#           tempamount = (p.quantity * p.product.discounted_price)
#           amount = amount + tempamount
           
#        data={
#            'amount':amount,
#            'totalamount':amount + shipping_amount
#        } 
 #       return JsonResponse(data)  


def remove_wishlist(request, pk):
    wishlists = Wishlist.objects.filter(id=pk)
    wishlists.delete()
    messages.success(request, 'Product delete Successfully')
    return redirect("/wishlist")



@login_required
def search(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
     totalitem = len(Cart.objects.filter(user=request.user))
     wishitem = len(Wishlist.objects.filter(user=request.user))
     query = request.GET['query']
     product = Product.objects.filter(title__icontains = query)
     context = {
        'product':product,
        'totalitem':totalitem,
        'wishitem':wishitem
     }
    return render(request, "app/search.html",context) 


@login_required
def add_to_wishlist(request):
     user = request.user
     product_id = request.GET.get('prod_id')
     product = Product.objects.get(id=product_id)
     Wishlist(user=user,product=product).save()
     return redirect("/wishlist")

@login_required
def show_wishlist(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
      totalitem = len(Cart.objects.filter(user=request.user))
      wishitem = len(Wishlist.objects.filter(user=request.user))
      user = request.user
      wishlist = Wishlist.objects.filter(user=user)
      #cart_product = [p for p in Wishlist.objects.all() if p.user == user]
      if wishlist:
         return render(request, 'app/wishlist.html',{'wishlists':wishlist,'wishitem':wishitem,'totalitem':totalitem})
      else:
          return render(request, 'app/emptywishlist.html',{'totalitem':totalitem,'wishitem':wishitem})




    



        
      
        