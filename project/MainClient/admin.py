from django.contrib import admin
from .models import CustomerProfile, Items, Wallet,Address, Orderss,CartItems
from . import models

class CustomerAdmin(admin.ModelAdmin):
    pass
class ItemsAdmin(admin.ModelAdmin):
    pass
class WalletAdmin(admin.ModelAdmin):
    pass
class AddressAdmin(admin.ModelAdmin):
    pass
class CartItemsAdmin(admin.ModelAdmin):
    pass
class OrderssAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(models.CustomerProfile,CustomerAdmin)
admin.site.register(models.Items,ItemsAdmin)
admin.site.register(models.Wallet,WalletAdmin)
admin.site.register(models.Address,AddressAdmin)
admin.site.register(models.Orderss,OrderssAdmin)
admin.site.register(models.CartItems,CartItemsAdmin)

