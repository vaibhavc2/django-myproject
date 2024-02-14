from django.urls import path, re_path
from . import views
from .views import restro
urlpatterns = [
    path('', views.home),  # Add this line to handle the empty path
    # path('hello/', views.hello),
    # path('hello/', views.hello),
    # path('home/', views.home),
    # path('dish/', views.menuitem),
    # path('dishes/', views.menuitems),
    # path('greet/<str:name>', views.greet),
    # path('food/<str:food>', views.foods),
    # path('add/<int:num1>/<int:num2>/', views.add_numbers,),
    # path('add/', views.add),
    # path('calculate/', views.calculate),
    # re_path(r'^user/(?P<username>[a-zA-Z]*)/?$', views.user_profile),
    # re_path(r'^item/(?P<item_id>\d+)/$', views.items),
    # re_path(r'^info/(?P<month>\d{1,2})/(?P<year>\d{4})/$', views.info_view),
    # re_path(r'^post/(?P<post>[\w-]+)/$', views.post),
    # path('menu/<str:category>/', views.menu_category),
    # path('menu/<str:category>/<str:subcategory>/', views.menu_subcategory),
    # path('restro/', restro, name='restro'),
    # path('menu/<str:item_name>/',  restro, name='restro'),
    path('home/', views.home, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('food/', views.food, name='food'), 
    path('food_detail/<str:item_name>/', views.food_detail, name='food_detail'),

]