from django.shortcuts import render,redirect
from users.models import Schedule, Users, Posts
from Stores.models import Store, Order
from Doctors.models import Slot
import datetime

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                Users.objects.get(username = request.POST['username'])
                return render (request,'users/register.html', {'error':'Username is already taken!'})
            except Users.DoesNotExist:
                user = Users(request.POST['name'], request.POST['username'], request.POST['email'], request.POST['contact'], password = request.POST['password1'])
                user.save()
                return redirect('users:dashboard', getattr(user, 'username'))
        else:
            return render (request,'users/register.html', {'error':'Passwords does not match!'})
    else:
        return render(request,'users/register.html')


def login(request):
    if request.method == 'POST':
        user = Users.objects.get(username=request.POST.get('username'))
        if user is None:
            return render(request, 'users/login.html', {'error':'No account with this username exist!'})
        else:
            if request.POST.get('password') == getattr(user, 'password'):
                return redirect('users:dashboard', getattr(user, 'username'))
            else:
                return render(request,'users/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'users/login.html')


def logout(request):
    return render(request, 'index.html')


def dashboard(request, name):
    if request.method == 'POST':
        start = request.POST['start_date']
        end = request.POST['end_date']

        start_date = datetime.datetime.strptime(start,'%Y-%m-%d')
        end_date = datetime.datetime.strptime(end,'%Y-%m-%d')
        schedule = Schedule(start_date=start_date, end_date=end_date, user = name)
        schedule.save()
        return redirect('users:dashboard', name)
    schedule = Schedule.objects.filter(user = name).order_by('id')[:5:-1]
    return render(request, 'users/dashboard.html', {'user': name, 'list': schedule})


def doctors(request, name):
    slots_list = Slot.objects.filter(status= 'Available')
    return render(request, 'users/doctor.html', {'list': slots_list, 'user': name})

def book_slot(request, name, slot_id):
    slot = Slot.objects.get(id = slot_id)
    user = Users.objects.get(name = name)
    slot.patient = name
    slot.patient_contact = user.contact
    slot.status = 'Booked'
    slot.save()
    return redirect('users:doctors', name)

def stores(request, name):
    stores_list = Store.objects.all()
    return render(request, 'users/stores.html', {'user': name, 'list': stores_list})

def place_order(request, name, store):
    if request.method == 'POST':
        order = Order(store=store, customer=name, address=request.POST.get('address'), items=request.POST.get('items'))
        order.save()
        return redirect('users:stores', name)
    orders = Order.objects.filter(store=store, customer=name)
    return render(request, 'users/order.html', {'user':name, 'store':store, 'list':orders})


def stories(request, name):
    return render(request, 'users/stories.html', {'user':name})


def write_story(request, name):
    if request.method == 'POST':
        story = Posts(title=request.POST['title'], author=name, content=request.POST['story'])
        story.save()
        return render(request, 'users/stories.html', {'user':name})
    return render(request, 'users/write_portal.html', {'user':name})


def view_story_list(request, name):
    story_list = Posts.objects.all()
    return render(request, 'users/read_portal.html', {'user':name, 'list':story_list})


def read_story(request, name, story_id):
    story = Posts.objects.get(id = story_id)
    return render(request, 'users/story_view.html', {'user':name, 'story':story})




