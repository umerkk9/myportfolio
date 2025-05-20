from django.shortcuts import render
from .forms import ContactForm

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')
# Create your views here.

def contact_view(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()  # Clear the form
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form, 'success': success})