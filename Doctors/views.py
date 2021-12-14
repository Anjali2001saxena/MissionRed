import datetime
from django.shortcuts import redirect, render
from Doctors.models import Doctor, Slot

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                Doctor.objects.get(email = request.POST['email'])
                return render (request,'Doctors/register.html', {'error':'Account with this email already exist!'})
            except Doctor.DoesNotExist:
                user = Doctor(request.POST['name'], request.POST['email'], request.POST['contact'], request.POST['specialization'], request.POST['registeration'], password = request.POST['password1'])
                user.save()
                return redirect('Doctors:dashboard', getattr(user, 'name'))
        else:
            return render (request,'Doctors/register.html', {'error':'Passwords does not match!'})
    else:
        return render(request,'Doctors/register.html')


def login(request):
    if request.method == 'POST':
        user = Doctor.objects.get(email = request.POST.get('email'))
        if user is None:
            return render(request,'Doctors/login.html', {'error':'No account with this email exist!'})
        else:
            if request.POST.get('password') == getattr(user, 'password'):
                return redirect('Doctors:dashboard', getattr(user, 'name'))
            else:
                return render (request,'Doctors/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'Doctors/login.html')


def logout(request):
    return render(request, 'index.html')


def dashboard(request, name):
    doctor = Doctor.objects.get(name = name)

    if (request.method == 'POST') and (getattr(doctor, 'is_verified')==False):
        return render(request, 'Doctors/dashboard.html', {'user':name, 'message':"Wait for verification by admin to schedule appointments!!"})

    if (request.method == 'POST') and (getattr(doctor, 'is_verified')==True):
        date = request.POST['date']
        time = request.POST['time']

        timing = datetime.datetime.combine(datetime.datetime.strptime(date,"%Y-%m-%d"), datetime.datetime.strptime(time, "%H:%M").time())
        slots = Slot(slot = timing, doctor = name)
        slots.save()
    slots = Slot.objects.filter(doctor = name).order_by('slot')
    return render(request, 'Doctors/dashboard.html', {'user': name, 'list':slots})



