from django.shortcuts import render, get_object_or_404, redirect
from .models import Good, Cart
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from online_store.users.models import CustomUser
from django.contrib import messages
from django.db.models import Q
from django.contrib.gis.geoip2 import GeoIP2
f

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong password or username!')
    return render(request, 'core/login_user.html')


def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = CustomUser.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'core/register_user.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def home(request):
    ip_adress = request.META.get('REMOTE_ADDR')
    # if ip_adress:
    #     geo = GeoIP2()
    #     city = geo.city(ip_adress)
    #     print(city)

    print(ip_adress)

    user_query = None
    goods = Good.objects.all()
    auth = False
    if request.user.is_authenticated:
        auth = True

    query = request.GET.get("query")
    if query:
        user_query = Good.objects.filter(Q(name__icontains=query))

    return render(request, 'core/home.html', {'goods': goods, 'auth': auth, 'query': user_query})


def info(request, pk):
    good = get_object_or_404(Good, pk=pk)
    return render(request, 'core/good_info.html', {'good': good})


def add_good(request, pk):
    if request.method == 'POST':
        # amount = request.GET.get("amount_goods")
        cart = get_object_or_404(Cart, user=request.user)
        if cart is not None:
            good = Good.objects.filter(id=pk)
            cart.goods_list.add(good[0])
            return redirect('cart')
        else:
            good = Good.objects.filter(id=pk)
            cart = Cart(user=request.user, goods_list=good[0])
            cart.save()

            # cart.goods_list.add(good[0])
            return redirect('cart')


def remove_good(request, pk):
    if request.method == 'POST':
        cart = get_object_or_404(Cart, user=request.user)
        good = Good.objects.filter(id=pk)
        cart.goods_list.remove(good[0])
        return redirect('cart')


# Надо сделать проверку что можно посмотреть в карзину только если пользователь авторизован
# Если нет то он видет пустую карзину либо ничего не происхлдит
def cart(request):
    goods_in_cart = Cart.objects.filter(user=request.user)
    # print(goods_in_cart[1].goods.list)
    return render(request, "core/cart.html", {"cart": goods_in_cart})
