from datetime import timezone
from django.shortcuts import render
from django.views.generic import ListView,CreateView,TemplateView,UpdateView,DetailView
from .models import CustomerProfile, Items,Wallet, Address, CartItems,Orderss
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template import loader
from django.urls import reverse
from django.http import HttpResponseRedirect
import graphene
from graphene_django.views import GraphQLView
from .models import CustomerProfile




def LoggedUserId(request):
		id=request.Wallet.get('id')
		return id
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class WalletUpdateView(UpdateView):
	model=Wallet
	fields=["name","balance"]
	template_name="MainClient/walletform.html"
	def get_success_url(self):
		pk = self.object.pk
		return reverse('MainClient:customerprofile', kwargs={'pk': pk})
	

class WalletDetail(DetailView):
	template_name='MainClient/walletview.html'
	model=Wallet
	
class AddressesView(UpdateView):
	model =Address
	fields=['title','city',"street","zipcode","apartment_no","daire"]
	template_name="MainClient/AddressUpdate.html"
	success_url='customerSide/home'

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('/customerSide/home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('/customerSide/login')
			

		context = {'form':form}
		return render(request, 'MainClient/registerform.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/customerSide/home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/customerSide/home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'MainClient/loginform.html', context)
		
     
class HomeView(TemplateView):
	template_name='MainClient/home.html'
	model=Address
	
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(HomeView, self).dispatch(*args, **kwargs)
	

class ItemsCreateView(CreateView):
	template_name='MainClient/itemupload.html'
	success_url='/itemupload'
	model=Items
	fields=['title','price','description','image']

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ItemsCreateView, self).dispatch(*args, **kwargs)
	@method_decorator(user_passes_test(lambda u: u.is_superuser))
	def dispatch(self, *args, **kwargs):
		return super(ItemsCreateView, self).dispatch(*args, **kwargs)
	
class CustomerProfileView(DetailView):
	template_name='MainClient/customerprofile.html'
	model=CustomerProfile
	context_object_name = 'customer'

class ItemListView(ListView):
	model=Items
	paginate_by=10
	template_name='MainClient/itemlist.html'



class ItemDetailView(DetailView):
	model=Items
	template_name='MainClient/itemdetail.html'

def add_to_cart(request, slug):
    item = get_object_or_404(Items, slug=slug)
    cart_item, created = CartItems.objects.get_or_create(
        user=request.user,
        item=item,
        ordered=False
    )
    if not created:
        # update the quantity of the item
        cart_item.quantity += 1
        cart_item.save()
    return redirect('MainClient:items')

def remove_from_cart(request, slug):
    item = get_object_or_404(Items, slug=slug)
    cart_item = get_object_or_404(CartItems, user=request.user, item=item, ordered=False)
    if cart_item.quantity > 1:
        # reduce the quantity of the item
        cart_item.quantity -= 1
        cart_item.save()
    else:
        # delete the cart item
        cart_item.delete()
    return redirect('MainClient:cart')

def create_order(request):
    if request.user.is_authenticated:
        cart_items = CartItems.objects.filter(user=request.user, ordered=False)
        if cart_items.exists():
            # get the user's wallet and calculate the total price of the items in the cart
            wallet = Wallet.objects.get(user=request.user)
            total_price = 0
            for item in cart_items:
                total_price += item.total_price()
            # check if the balance in the wallet is enough to make the purchase
            if total_price <= wallet.balance:
                # get the shipping address for the user
                shipping_address = Address.objects.get(user=request.user)

                # create the Order object
                order = Orderss.objects.create(
                    user=request.user,
                    ordered_date=timezone.now(),
                    shipping_address=shipping_address
                )

                # add the cart items to the order
                order.items.add(*cart_items)
                order.save()

                # set the ordered field to True for the cart items
                for item in cart_items:
                    item.ordered = True
                    item.save()

                # update the balance in the wallet
                wallet.balance -= total_price
                wallet.save()
			
                return redirect('MainClient:cart')
            else:
                messages.warning(request, "Your balance is not enough to make this purchase")
                return redirect('MainClient:cart')
        else:
            messages.warning(request, "You don't have any items in your cart")
            return redirect('MainClient:cart')
    else:
        messages.warning(request, "You must be logged in to create an order")
        return redirect



def cart_view(request):
    cart_items = CartItems.objects.filter(user=request.user, ordered=False)
    total_price = 0
    for cart_item in cart_items:
        total_price += cart_item.item.price * cart_item.quantity
    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'MainClient/cart.html', context)


def welcome(request):
    if request.user.is_authenticated:
        return redirect('customerSide/home')
    else:
        return render(request, 'MainClient/welcome.html')
 
def previous_orders_view(request):
    orders = Orderss.objects.filter(user=request.user)
    context = {
        'orders': []
    }
    for order in orders:
        total_price = 0
        for item in order.items.all():
            total_price += item.total_price()
        context['orders'].append({'order': order, 'total_price': total_price})
    return render(request, 'MainClient/previous_orders.html', context)

def checkout(ItemDetailView):
    pass



def logout_view(request):
    logout(request)
    return redirect('project:welcome')


def thanks(request):
    return render(request, 'thanks.html')

	



