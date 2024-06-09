
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm


urlpatterns = [
    path("", views.ProductView.as_view(),name="home"),
    path("about/", views.About,name="about"),
    path("contact/", views.Contact,name="contact"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(),name="product-detail"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('updateaddress/<int:pk>', views.Updateaddress.as_view(), name='updateaddress'),
           #Laptop
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
           #Mobile
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
           #Soundbox
    path('soundbox/', views.soundbox, name='soundbox'),
    path('soundbox/<slug:data>', views.soundbox, name='soundboxdata'),

    path('address/', views.Address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
   
    path('add-to-wishlist/', views.add_to_wishlist, name='add-to-wishlist'),
    path('wishlist/', views.show_wishlist, name='show-wishlist'),
    path('removewishlist/<int:pk>', views.remove_wishlist, name='removewishlist'),
    path('deleteaddress/<int:pk>', views.delete_address, name='deleteaddress'),
    path('cart/', views.show_cart, name='showcart'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('paymentdone2/', views.payment_done2, name='paymentdone2'),
    path('checkout/', views.Checkout.as_view(), name='checkout'),
    path('checkout2/<int:pk>', views.Checkout2.as_view(), name='checkout2'),
    path('search/', views.search, name='search'),

    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    
  
       #authentication
    path("logout/", auth_view.LogoutView.as_view(next_page='login'),name="logout"),   
    path("registration", views.Registration.as_view(),name="registration"),   
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
       #change password 
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
       #forget password
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)