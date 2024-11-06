

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Su mensaje ha sido enviado con éxito.')
            return redirect('home.html')
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})
