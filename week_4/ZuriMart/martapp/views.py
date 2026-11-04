from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    # Data we want to send to the HTML template
    my_data = {
        'page_heading': 'Our Services',
        'service_list': ['Web Development', 'Cloud Hosting', 'UI Design'],
    }
    # Load services.html and inject my_data into it
    return render(request, 'services.html', my_data)