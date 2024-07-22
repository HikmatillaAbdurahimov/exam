from django.urls import  path
from startapp.views import home_view,product_view,contact_view,shop_detail,pages_view,chackout_view,cart_view,testimonial_view


urlpatterns=[
    path('',home_view,name='home'),
    path('product/',product_view,name='product'),
    path('contact/', contact_view,name='contact'),
    path('shop_detail/',shop_detail,name='shop_detail'),
    path('cart/',cart_view,name='cart'),
    path('chackout/',chackout_view,name='chackout'),
    path('testimonial/',testimonial_view,name='testimonial'),
    path('pages/',pages_view,name='pages'),

]


