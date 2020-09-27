from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from datetime import date
# Create your views here.
def Home(request):
    cat = Category.objects.all()
    d = {'cat': cat}
    return render(request, 'index.html', d)

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Logout(request):
    if not request.user.is_authenticated:
        return redirect('login')
    logout(request)
    return redirect('home')


def Login(request):
    error = False
    try:
        if not request.user.is_staff:
            if request.method == 'POST':
                u = request.POST['uname']
                p = request.POST['psw']
                user = authenticate(username=u, password=p)
                if not user.is_staff:
                    login(request, user)
                    return redirect('home')
                else:
                    error = True
    except:
        error = True

    d = {'error': error}
    return render(request, 'login.html', d)



def Add_Profile(request):
    error = False
    if request.method == 'POST':
        n = request.POST['name']
        u = request.POST['uname']
        p = request.POST['pwd']
        d = request.POST['date']
        c = request.POST['city']
        ad = request.POST['add']
        e = request.POST['email']
        con = request.POST['contact']
        user1 = User.objects.filter(username = u)
        if user1:
            error = True
        else:
            user = User.objects.create_user(username=u, email=e, password=p, first_name=n)
            Profile.objects.create(user=user, dob=d, city=c, address=ad, contact=con)
            return redirect('login')
    d = {'error':error}
    return render(request, 'profile.html',d)

def Login_Admin(request):
    error = False
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['psw']
        user = authenticate(username=u, password=p)
        if user.is_staff:
            login(request, user)
            return redirect('admin_base')
        else:
            error = True
    d = {'error': error}

    return render(request, 'login_admin.html', d)

def Admin_Base(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    book=Booking.objects.all()
    pro=Product.objects.all()
    profile=Profile.objects.all()
    b=0
    b1=0
    b2=0
    for i in book:
        b+=1
    for j in pro:
        b1+=1
    for k in profile:
        b2+=1
    d={'b':b,'b1':b1,'b2':b2}
    return render(request, 'admin_home.html',d)
def Admin_Profile(request, pid):
    if not request.user.is_staff:
        return redirect('login_admin')
    user1 = User.objects.get(id=pid)
    data = Profile.objects.filter(user=user1).first()
    d = {'data': data}
    return render(request, 'admin_profile.html', d)


def View_Product(request):

    pro = Product.objects.all()
    d = {'pro': pro}
    return render(request, 'view_product.html', d)
def View_Categary(request):

    pro = Category.objects.all()
    d = {'pro': pro}
    return render(request, 'view_category.html', d)
def Admin_View_Product(request):

    pro = Product.objects.all()
    d = {'pro': pro}
    return render(request, 'admin_view_product.html', d)

def Product_booking(request,pid):
    pro1 = Category.objects.get(id=pid)
    pro=Product.objects.filter(category=pro1)
    d = {'pro': pro}
    return render(request, 'basekin.html', d)
def Add_Product(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    cat = Category.objects.all()
    error=False
    if request.method=="POST":
        c = request.POST['cat']
        p = request.POST['pname']
        pr = request.POST['price']
        i = request.FILES['img']
        d = request.POST['desc']
        ct = Category.objects.filter(name=c).first()
        Product.objects.create(category=ct, name=p, price=pr, image=i, desc=d)
        error=True
    d = {'cat': cat,'error':error}
    return render(request, 'add_product.html', d)
def Add_Categary(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    error=False
    if request.method=="POST":
        n = request.POST['name']
        i = request.FILES['img']
        Category.objects.create(name=n,image=i)
        error=True
    d = {'error':error}
    return render(request, 'add_categary.html', d)

def Admin_View_Booking(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    book = Booking.objects.all()
    d = {'book': book}
    return render(request, 'admin_viewBokking.html', d)

def View_feedback(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    feed = Send_Feedback.objects.all()
    d = {'feed': feed}
    return render(request, 'view_feedback.html', d)
def Logout_Admin(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    logout(request)
    return redirect('login_admin')

def View_Customer(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    cust = Profile.objects.all()
    d = {'cus': cust}
    return render(request, 'view_customer.html', d)
def Edit_Product(request, pid):
    if not request.user.is_staff:
        return redirect('login_admin')
    pro = Product.objects.get(id=pid)
    cat = Category.objects.all()
    error=False
    if request.method=="POST":
        p = request.POST['pname']
        pr = request.POST['price']
        d = request.POST['desc']
        pro.name = p
        pro.price = pr
        pro.desc = d
        pro.save()
        try:
            c = request.POST['cat']
            ct = Category.objects.filter(name=c).first()
            pro.category = ct
            pro.save()
        except:
            pass
        try:
            i = request.FILES['img']
            pro.image = i
            pro.save()
        except:
            pass
        error=True
    d = {'cat': cat, 'pro': pro,'error':error}
    return render(request, 'edit_product.html', d)
def delete_product(request,pid):
    if not request.user.is_staff:
        return redirect('login_admin')
    if Product.objects.filter(id=pid).exists():
        pro = Product.objects.get(id=pid)
        pro.delete()
        message1 = messages.info(request, 'Product Cancelled')
        return redirect('admin_view_product')
def delete_categary(request,pid):
    if not request.user.is_staff:
        return redirect('login_admin')
    if Category.objects.filter(id=pid).exists():
        pro = Category.objects.get(id=pid)
        pro.delete()
        message1 = messages.info(request, 'Category Cancelled')
        return redirect('view_categary')
def Delete_Customer(request, pid):
    if not request.user.is_staff:
        return redirect('login_admin')
    if Profile.objects.filter(id=pid).exists():
        pro = Profile.objects.get(id=pid)
        pro.delete()
        message1 = messages.info(request, 'Customer Deleted')
        return redirect('view_customer')
def Edit_Profile(request, pid):
    data = Profile.objects.get(id=pid)
    if request.method == 'POST':
        n = request.POST['name']
        u = request.POST['uname']
        c = request.POST['city']
        ad = request.POST['add']
        e = request.POST['email']
        con = request.POST['contact']
        data.user.first_name = n
        data.user.username = u
        data.user.email = e
        data.contact = con
        data.address = ad
        data.city = c
        data.save()
        try:
            d = request.POST['date']
            data.dob = d
            data.save()
        except:
            pass

        return redirect('view_prifile')
    d = {'data': data}
    return render(request, 'edit_profile.html', d)



def View_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data1 = User.objects.get(id=request.user.id)
    data = Profile.objects.filter(user=data1).first()
    d = {'data': data}
    return render(request, 'view_profile.html', d)

def Booking_order(request, pid):
    if not request.user.is_authenticated:
        return redirect('login')
    pro = Product.objects.get(id=pid)
    pro1=Profile.objects.get(user=request.user.id)

    data1 = User.objects.get(id=request.user.id)
    data = Profile.objects.filter(user=data1).first()
    date1 = date.today()
    if request.method == "POST":
        d = request.POST['date']
        c = request.POST['name']
        c1 = request.POST['city']
        ad = request.POST['add']
        e = request.POST['email']
        con = request.POST['contact']
        p = request.POST['pname']
        pr = request.POST['price']
        q = request.POST['quantity']
        t = request.POST['total']
        stat=Status.objects.get(name="pending")

        Book = Booking.objects.create(user=request.user,status=stat, book_date=d, c_name=c, email=e, contact=con, city=c1, address=ad, pro_name=p, price=pr, quantity=q, total=t)


        return redirect('payment1',Book.id)


    d = {'data': data, 'data1': data1, 'pro': pro, 'date1': date1, 'pro1': pro1}

    return render(request, 'booking.html', d)

def View_Booking(request):
    book = Booking.objects.filter(user=request.user)
    if book:
        pass
    else:
        message1 = messages.info(request, 'Not Found Any Data Related To Order')

    d = {'book': book}
    return render(request, 'view_booking.html', d)

def delete_booking(request, pid):
    if not request.user.is_authenticated:
        return redirect('login')
    book = Booking.objects.get(id=pid)
    book.delete()
    message2 = messages.info(request, 'Booking Cancelled')
    return redirect('view_booking')
def Payment1(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    book = Booking.objects.get(id=pid)

    message1 = messages.info(request, 'Booking Your Order Successfully')
    d = {'book': book}
    return render(request, 'payment2.html', d)

def Payment(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'payment2.html')
def View_feedback(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    feed = Send_Feedback.objects.all()
    d = {'feed': feed}
    return render(request, 'view_feedback.html', d)
def Admin_View_Booking(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    book = Booking.objects.all()
    d = {'book': book}
    return render(request, 'admin_viewBokking.html', d)
def Feedback(request, pid):
    if not request.user.is_authenticated:
        return redirect('login')
    date1 = date.today()
    user = User.objects.get(id=pid)
    pro = Profile.objects.filter(user=user).first()
    if request.method == "POST":
        d = request.POST['date']
        u = request.POST['name']
        e = request.POST['email']
        con = request.POST['contact']
        m = request.POST['message']
        user = User.objects.filter(username=u, email=e).first()
        pro = Profile.objects.filter(user=user, contact=con).first()
        Send_Feedback.objects.create(profile=pro, date=d, message1=m)
        message1 = messages.info(request, 'send_feedback successfully')
        return redirect('send_feedback',pid)

    d = {'pro': pro, 'date1': date1}

    return render(request, 'feedback.html', d)

def Delete_feedback(request, pid):
    if not request.user.is_staff:
        return redirect('login_admin')
    if Send_Feedback.objects.filter(id=pid).exists():
        pro = Send_Feedback.objects.get(id=pid)
        pro.delete()
        message1 = messages.info(request, 'Selected Feedback Deleted')
        return redirect('view_feedback')

def Edit_status(request,pid):
    if not request.user.is_staff:
        return redirect('login_admin')
    book = Booking.objects.get(id=pid)
    stat = Status.objects.all()
    if request.method == "POST":
        n = request.POST['book']
        s = request.POST['st']
        book.id = n
        sta = Status.objects.filter(name=s).first()
        book.status = sta
        book.save()
        return redirect('admin_viewBooking')

    d = {'book': book, 'stat': stat}
    return render(request, 'status.html', d)
def change_password(request):
     error=""
     data = User.objects.get(username=request.user.username)
     if request.method=="POST":
        o=request.POST['password1']
        n=request.POST['password2']
        if o==n:
            data.set_password(o)
            data.save()
            login(request,data)
            error="yes"
            return redirect('login')
        else:
            error="not"
     d={'error':error}
     return render(request,'change_password.html',d)

