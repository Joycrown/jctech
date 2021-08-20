from django.shortcuts import render


# Create your views here.
def home(request):

    return render(request, 'home.html', {})



   
   

def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        return render(request, 'home.html')



    else:
        return render(request, 'home.html', {})