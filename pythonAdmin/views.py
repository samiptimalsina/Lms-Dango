from django.http import HttpResponse
from django.shortcuts import render
from .forms import UsersForm
def Home(request):
    data={
        'arr':['Apple','Orange','mobile','Laptop','Desktop'],
        "students":[
            {"name":"Rahul","age":20,"city":"Delhi" ,"phone":"9860305035"},
            {"name":"Rohan","age":21,"city":"Mumbai","phone":"9860304035"},
            {"name":"Rahul","age":22,"city":"Kolkata","phone":"9860109035"},
            {"name":"Rohan","age":23,"city":"Chennai","phone":"986009035"},


        ]

    }
    return render(request, 'front/index.html')

def About(request):
    return render(request, 'front/about.html')

def Services(request):
    return render(request,'front/service.html')

def Team(request):
    return render(request,'front/team.html')

def WhyUs(request):
    return render(request,'front/why.html')

def Course(request, courseId):
    return HttpResponse("Welcome to course page " + str(courseId))

def contactUs(request):
    if request.method == 'POST':
        print(request.POST)  # Correctly indented

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not name or not email or not subject or not message:
            context = {
                'error': 'All fields are required.',
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            }
            return render(request, 'front/contact.html', context)

        context = {
            'success': 'Your message has been sent successfully!',
        }
        return render(request, 'front/contact.html', context)

    return render(request, 'front/contact.html')
