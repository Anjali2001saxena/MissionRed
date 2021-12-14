from django.shortcuts import redirect, render
from Stores.models import Order, Store

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                Store.objects.get(email = request.POST['email'])
                return render (request,'Stores/register.html', {'error':'Account with this email already exist!'})
            except Store.DoesNotExist:
                if request.POST['delivery'] == 'on':
                    delivery = True
                else:
                    delivery = False
                store = Store(request.POST['name'], request.POST['owner'], request.POST['email'], request.POST['contact'], request.POST['location'], request.POST['pincode'], delivery, password = request.POST['password1'])
                store.save()
                return redirect('Stores:dashboard', request.POST['name'])
        else:
            return render (request,'Stores/register.html', {'error':'Passwords does not match!'})
    else:
        return render(request,'Stores/register.html')


def login(request):
    if request.method == 'POST':
        store = Store.objects.get(email=request.POST.get('email'))
        if store is None:
            return render(request, 'Stores/login.html', {'error':'No account with this email exist!'})
        else:
            if request.POST.get('password')== getattr(store, 'password'):
                return redirect('Stores:dashboard', getattr(store, 'name'))
            else:
                return render (request,'Stores/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'Stores/login.html')


def logout(request):
    return render(request, 'index.html')


def dashboard(request, name):
    orders = Order.objects.filter(store = name, status = 'Pending').order_by('timing')
    return render(request, 'Stores/dashboard.html', {'user':name, 'list': orders})

def deliver_order(request, name, order_id):
    order = Order.objects.get(id = order_id)
    order.status = 'Delivered'
    order.save()
    return redirect('Stores:dashboard', name)

def cancel_order(request, name, order_id):
    order = Order.objects.get(id = order_id)
    order.status = 'Canceled'
    order.save()
    return redirect('Stores:dashboard', name)

