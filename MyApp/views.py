from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import TheWebsiteInfo
from .models import TheWebsiteImages
from .models import TheWebsiteAboutText
from .models import TheWebsiteTrainers
from .models import TheWebsiteCourses
from .models import TheWebsitePricing
from .models import TheWebsiteTestimonials



# Create your views here.
def index(request):
    #return HttpResponse ("<h1> Hello </h1>")
    context = {'data': {
        "TheWebsiteInfo" : TheWebsiteInfo.objects.get(pk=1),
        "TheWebsiteImages" : TheWebsiteImages.objects.all(),
        "TheWebsiteAboutText": TheWebsiteAboutText.objects.all(),
        "TheWebsiteTrainers": TheWebsiteTrainers.objects.all(),
        "TheWebsiteCourses" : TheWebsiteCourses.objects.all()
    }}
    return render(request, 'index.html',context)

def pricing(request):
    return render(request, 'pricing.html')

def about(request):
    #context = { "TheWebsiteInfo" : TheWebsiteInfo.objects.get(pk=1)}
    context = {'data': {
    "TheWebsiteInfo" : TheWebsiteInfo.objects.get(pk=1),
    "TheWebsiteImages" : TheWebsiteImages.objects.all(),
    "TheWebsiteAboutText": TheWebsiteAboutText.objects.all(),
    "TheWebsiteTestimonials": TheWebsiteTestimonials.objects.all()
    }}
    return render(request, 'about.html',context)

def courses(request):
    context = {'data': {
        "TheWebsiteCourses" : TheWebsiteCourses.objects.all()}}
    return render(request, 'courses.html', context)

def trainers(request):
    context = {'data': {
        "TheWebsiteInfo" : TheWebsiteInfo.objects.all(),
        "TheWebsiteImages" : TheWebsiteImages.objects.all(),
        "TheWebsiteAboutText": TheWebsiteAboutText.objects.all(),
        "TheWebsiteTrainers": TheWebsiteTrainers.objects.all()
    }}
    return render(request, 'trainers.html',context)

def events(request):
    #context = { "TheWebsiteImages" : TheWebsiteImages.objects.get(pk=1)}
    context = {'data': {
        "TheWebsiteInfo" : TheWebsiteInfo.objects.all(),
        "TheWebsiteImages" : TheWebsiteImages.objects.all(),
        "TheWebsiteAboutText": TheWebsiteAboutText.objects.all(),
        "TheWebsiteTrainers": TheWebsiteTrainers.objects.all(),
        "TheWebsiteCourses" : TheWebsiteCourses.objects.all()
    }}
    return render(request, 'testing.html',context)

def coursedetails(request,pk):
    TheCourse = TheWebsiteCourses.objects.get(id=pk).Title

    context = {"TheWebsiteCourses" : TheWebsiteCourses.objects.get(id=pk),
    "TheWebsitePricing": TheWebsitePricing.objects.filter(CourseTitle=TheCourse)
    }
    return render(request,'course-details.html',context)

def contact(request):
    context = {'data': {
        "TheWebsiteAboutText": TheWebsiteAboutText.objects.all()
    }}
    return render (request, 'contact.html',context)

def send_email(request):
    if request.method == 'POST':
        # Get the form data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        subject = ("EMAIL: ")+email+(" | ")+("SUBJECT: ")+subject

        # Create and send the email
        try:
            send_mail(
                subject,
                message,
                email,
                ['thrint58@gmail.com','branchouttutoringteam@gmail.com']
            )
            return HttpResponse('OK')
        except Exception as e:
            return HttpResponse("Failed to send email: {}".format(str(e)))

    return HttpResponse("Invalid request method. Please use a POST request to send an email.")
            

            #return JsonResponse({'status': 'success', 'message': 'Email sent successfully.'})
        #except Exception as e:
        #    return JsonResponse({ 'message': 'Failed to send email: ' + str(e)})

    #return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


