from django.urls import path
from faster import views
app_name="faster"

urlpatterns = [
    path('', views.Home, name='home'),
    path('login/', views.loginU, name='login'),
    path('About', views.About, name="About"),
    path('Base', views.Base, name="Base"),
    path('Blog', views.Blog, name="Blog"),
    path('Contact', views.Contact, name="Contact"),
    path('Price', views.Price, name="Price"),
    path('Service', views.Service, name="Service"),
    path('Single', views.Single, name="Single"),
    path('Team', views.Team, name="Team"),
    path('Account', views.Account, name="Account"),
    path('Checkout', views.Checkout, name="Checkout"),
    path('Thankyou', views.Thankyou, name="Thankyou"),
]