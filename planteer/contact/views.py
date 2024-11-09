from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:contact_us')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_us.html', {
        'form': form
    })

def contact_messages(request):
    messages = Contact.objects.all().order_by('-created_at')
    return render(request, 'contact/contact_messages.html', {'messages': messages})
