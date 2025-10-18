from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from student.models import sinfoin,act

def home(request):
    return render(request,'index.html')

def clas(request):
    return render(request,'class.html')
def about(request):
    return render(request,'about.html')

def cont(request):
    return render(request,'contact.html')
def reg(request):
    try:
        if request.method == 'POST':
            namef = request.POST.get('fname')
            phonef = request.POST.get('phonen')
            emailf = request.POST.get('email')
            passw = request.POST.get('password')

            # Check if a user with the given name or email already exists
            username = sinfoin.objects.filter(name=namef).exists()
            useremail = sinfoin.objects.filter(email=emailf).exists()

            if not username and not useremail:
                # If neither name nor email exists, create a new user
                data = sinfoin(name=namef, phone=phonef, email=emailf, password=passw)
                data.save()
                return redirect('login')
            elif username:
                return HttpResponse("This name is already taken. Please enter a new name.")
            elif useremail:
                return HttpResponse("This email is already taken. Please enter a new email.")
    except Exception as e:
        # Print or log the exception for debugging purposes
        print(e)

    return render(request, 'register.html')

def login(request):
    data = sinfoin.objects.all().values('name', 'email', 'password')

    if request.method == 'POST':
        email = request.POST['email']
        passw = request.POST['password']

        # Use a flag to check if a valid user is found
        valid_user = False

        for req in data:
            em = req['email']
            pa = req['password']
            na = req['name']

            if em == email and pa == passw:
                # Set the flag and break out of the loop
                valid_user = True
                request.session['user_name'] = na
                break

        if valid_user:
            return redirect('Ahome')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')  # Redirect to your login page

    return render(request, 'login.html')

def Logout(request):
    # Clear the session variable
    if 'user_name' in request.session:
        del request.session['user_name']
    # Redirect to your logout page or home page
    return redirect('home')

def Ahome(request):
    ndata = request.session.get('user_name')
    return render(request, 'Aindex.html', {'name': ndata})

def Aabout(request):
    ndata = request.session.get('user_name')
    return render(request,'Aabout.html',{'name': ndata})

def Acont(request):
    ndata = request.session.get('user_name')
    return render(request,'Acontact.html',{'name': ndata})

def Aclas(request):
    ndata = request.session.get('user_name')
    return render(request,'Aclass.html',{'name': ndata})

def class4(request):
    return render(request, 'class4.html')
    
def math4(request):
    return render(request, 'math4.html')
def m4ch1(request):
    return render(request, 'm4/chapter1M4.html')
def m4ch2(request):
    return render(request, 'm4/chapter2M4.html')
def m4ch3(request):
    return render(request, 'm4/chapter3M4.html')
def m4ch4(request):
    return render(request, 'm4/chapter4M4.html')
def m4ch5(request):
    return render(request, 'm4/chapter5M4.html')
def m4ch6(request):
    return render(request, 'm4/chapter6M4.html')
def m4ch7(request):
    return render(request, 'm4/chapter7M4.html')
def m4ch8(request):
    return render(request, 'm4/chapter8M4.html')
def m4ch9(request):
    return render(request, 'm4/chapter9M4.html')
def m4ch10(request):
    return render(request, 'm4/chapter10M4.html')
def m4ch11(request):
    return render(request, 'm4/chapter11M4.html')
def m4ch12(request):
    return render(request, 'm4/chapter12M4.html')
def m4ch13(request):
    return render(request, 'm4/chapter13M4.html')

def bangla4(request):
    return render(request, 'bangla4.html')
def b4ch1(request):
    return render(request, 'b4/chapter1.html')
def b4ch2(request):
    return render(request, 'b4/chapter2.html')
def b4ch3(request):
    return render(request, 'b4/chapter3.html')
def b4ch4(request):
    return render(request, 'b4/chapter4.html')
def b4ch5(request):
    return render(request, 'b4/chapter5.html')
def b4ch6(request):
    return render(request, 'b4/chapter6.html')
def b4ch7(request):
    return render(request, 'b4/chapter7.html')
def b4ch8(request):
    return render(request, 'b4/chapter8.html')
def b4ch9(request):
    return render(request, 'b4/chapter9.html')
def b4ch10(request):
    return render(request, 'b4/chapter10.html')
def b4ch11(request):
    return render(request, 'b4/chapter11.html')
def b4ch12(request):
    return render(request, 'b4/chapter12.html')
def b4ch13(request):
    return render(request, 'b4/chapter13.html')
def b4ch14(request):
    return render(request, 'b4/chapter14.html')
def b4ch15(request):
    return render(request, 'b4/chapter15.html')
def b4ch16(request):
    return render(request, 'b4/chapter16.html')
def b4ch17(request):
    return render(request, 'b4/chapter17.html')
def b4ch18(request):
    return render(request, 'b4/chapter18.html')
def b4ch19(request):
    return render(request, 'b4/chapter19.html')

def english4(request):
    return render(request, 'english4.html')
def e4ch1(request):
    return render(request, 'e4/chapter1.html')
def e4ch2(request):
    return render(request, 'e4/chapter2.html')
def e4ch3(request):
    return render(request, 'e4/chapter3.html')
def e4ch4(request):
    return render(request, 'e4/chapter4.html')
def e4ch5(request):
    return render(request, 'e4/chapter5.html')
def e4ch6(request):
    return render(request, 'e4/chapter6.html')
def e4ch7(request):
    return render(request, 'e4/chapter7.html')
def e4ch8(request):
    return render(request, 'e4/chapter8.html')
def e4ch9(request):
    return render(request, 'e4/chapter9.html')

def science4(request):
    return render(request, 'science4.html')
def s4ch1(request):
    return render(request, 's4/chapter1.html')
def s4ch2(request):
    return render(request, 's4/chapter2.html')
def s4ch3(request):
    return render(request, 's4/chapter3.html')
def s4ch4(request):
    return render(request, 's4/chapter4.html')
def s4ch5(request):
    return render(request, 's4/chapter5.html')
def s4ch6(request):
    return render(request, 's4/chapter6.html')

def religion4(request):
    return render(request, 'religion4.html')
def r4ch1(request):
    return render(request, 'r4/chapter1.html')
def r4ch2(request):
    return render(request, 'r4/chapter2.html')
def r4ch3(request):
    return render(request, 'r4/chapter3.html')
def r4ch4(request):
    return render(request, 'r4/chapter4.html')
def r4ch5(request):
    return render(request, 'r4/chapter5.html')


def class5(request):
    return render(request, 'class5.html')

def class6(request):
    return render(request, 'class6.html')

def class7(request):
    return render(request, 'class7.html')

def class8(request):
    return render(request, 'class8.html')



def ch2(request):
    return render(request, 'chapter2.html')

def pro(request):
    ndata = request.session.get('user_name')
    det=sinfoin.objects.get(name=ndata)
    return render(request,'profile.html',{'name': ndata,'data':det})

def demo(request):
    return render(request,'demo.html')