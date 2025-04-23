




from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as auth_logout
from .models import Work
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.


def extra(request):
    return render(request,'extra.html')


def base(request):
    return render(request,'base.html')

# def body(request):
    

#     return render(request,'body.html')


def body(request):
    context={}

    skip=Work.objects.all()
    print(skip)
    context["skip"]=skip


    return render(request,'body.html',context)
   


def story(request):
    return render(request,'story.html')


def partner(request):
    return render(request,'partner.html')  

def story_details(request, id):
    try:
        story = Work.objects.get(id=id)
    except Work.DoesNotExist:
        story = None  # Or handle the error how you want

    return render(request, 'story_details.html', {'story': story})



   



def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")  # Redirect to the dashboard or home page
        else:
            messages.error(request, "Invalid email or password")

    return render(request, "login.html")


def register(request):
    context={}
    if request.method=='POST':
        un=request.POST['uname']
        em=request.POST['uemail']
        p=request.POST['upass']
        cp=request.POST['ucpass']
        print(un,em,p,cp)
        if un=='' or em=='' or p=='' or cp=='':
            context['error_msg']='ALL FIELDS ARE REQUIRED'
            return render(request,'register.html',context)
       
        elif len(p)<8:
            context['error_msg']='PASSWORD MUST BE  GREATER THAN OR EQUAL TO 8'
            return render(request,'register.html',context)

        elif p!=cp:
            context['error_msg']='PASSWORD AND CONFIRM PASSWORD NOT MATCHED'
            return render(request,'register.html',context)

        else:
            u = User.objects.create(username=em, email=em)  # Use email as username

            u.set_password(p)
            u.save()

            return redirect('/login')
        



        
    else:
        return render(request,'register.html')



from django.contrib.auth import logout as auth_logout

def logout_view(request):
    auth_logout(request)
    return redirect('/login')





def donate(request):
    if request.method == "POST":
        amount = int(request.POST.get("amount")) * 100  # Convert to paisa

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        data = {
            "amount": amount,
            "currency": "INR",
            "receipt": "receipt_donation"
        }

        order = client.order.create(data=data)

        return render(request, "donate.html", {
            "order_id": order["id"],
            "amount": amount,
            "razorpay_key": settings.RAZORPAY_KEY_ID
        })

    return render(request, "donate.html")


# programs

def ujjwal(request):
    return render(request,'ujjwal.html')

def shiksha(request):
    return render(request,'shiksha.html')


def fly(request):
    return render(request,'fly.html')  


def volenteer(request):
    return render(request,'volenteer.html')     

def volunteer_form(request):
    return render(request, 'volunteer_form.html')


def submit_volunteer_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        availability = request.POST.get("availability")
        interest = request.POST.get("interest")
        message = request.POST.get("message")
        # You can save this to the DB or send an email
        return HttpResponse("Thank you for volunteering!")
    return redirect("body.html")       