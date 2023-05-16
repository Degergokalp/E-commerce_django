from django.urls import path
from graphene_django.views import GraphQLView
from django.contrib.auth import views as auth_views
from . import views
app_name='project'
urlpatterns=[ 
        
        path("wallet/<slug:slug>",views.WalletDetail.as_view(),name="wallet"),
        path('login', views.loginPage, name="loginPage"),
        path("home",views.HomeView.as_view(),name="home"),
        path('registration',views.registerPage,name='register.new'),
        path('itemupload',views.ItemsCreateView.as_view(),name="itemupload"),
        path('walletupdate/<slug:slug>',views.WalletUpdateView.as_view(),name="walletupdate"),
        path('customerprofile/<int:pk>/',views.CustomerProfileView.as_view(),name="customerprofile"),
        path('addressupdate/<slug:slug>',views.AddressesView.as_view(),name="addressupdate"),
        path('Items',views.ItemListView.as_view(),name='items'),
        path('Itemsdetail/<slug:slug>',views.ItemDetailView.as_view(),name='itemdetail'),
        path('add_to_cart/<slug:slug>',views.add_to_cart,name='add_to_cart'),
        path('thanks/', views.thanks, name='thanks'),
        path('cart',views.cart_view,name='cart'),
        path('remove_from_cart/<slug:slug>/', views.remove_from_cart, name='remove_from_cart'),
        path('create_order/', views.create_order, name='create_order'),
        path('logout',views.logout_view,name='logout'),
        path('previousorder',views.previous_orders_view,name='previousorder'),
        path('graphql', GraphQLView.as_view(graphiql=True)),
        path("checkout")
        


        
        
        
]