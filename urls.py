from django.contrib import admin
from django.urls import path,include
from account import views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

from account.forms import addCoustmer
from account.views import login, create_account, UserLoginAPIView, UserRegistrationAPIView, add_coustmer,dashboard,manage_Client,manage_sections,manage_prodect,add_productoffer,manage_order
# from .views import UserRegistrationView,UserLoginAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('',auth_views.LoginView.as_view(template_name='login.html'),name='login'),

    # path('login/',views.loginPage,name='login'),manage_Client
     path('dashboard/',dashboard,name='dashboard'),
    path('manage_client/',manage_Client,name='manage_client'),
     path('addcoustmer/',add_coustmer,name='addcoustmer'),
     path('adduser',views.add_user,name='addusers'),
    path('manage_prodect/',manage_prodect,name='manage_prodect'),
    path('manage_prodect/<int:Prodect_id>',views.add_productoffer,name='addproductoffer'),
     path('addprodect/',views.add_prodect,name='addprodect'),


    path('manage_order/',manage_order,name='manage_order'),


    path('addproductoffer/',views.add_productoffer,name='addproductoffer'),
     path('addsections/',views.add_sections,name='addsections'),
    path('manage_sections/',manage_sections,name='manage_sections'),
    path('api/',views.no_rest_no_model),
    path('api_all_user/',views.no_rest_from_model),
    path('api_fbv/',views.FBV_List),
    path('api_Address_List/',views.CBV_Address_List.as_view()),
    path('api_CBV_Get_All_Orders_List/',views.CBV_Get_All_Orders_List.as_view()),
    path('api_cbv/',views.CBV_List.as_view()),
    path('CBV_Cart_List/',views.CBV_Cart_List.as_view()),
    path('register/', create_account, name='user_registration'),
    path('login/', login, name='user_login'),
    # path("register/",views.UserRegistrationView.as_view()),
    path("get_user_data/", views.get_user_data),
    # path('api_CBV_ListOfOrders/',views.CBV_ListOfOrders.as_view()),
    path('api_cbvcatag/',views.CBVCatg_List.as_view()),
    path('api_CBVCoustemSections/',views.CBVCoustemSections_List.as_view()),
    path('api_CBVProdects_List/',views.CBVProdects_List.as_view()),
    path('viewProdect/',views.view_Prodect,name='viewProdect'),

    # path('api-token-auth', obtain_auth_token),
    path('rest/generics/', views.generics_list.as_view()),
]
