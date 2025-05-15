from django.shortcuts import render, redirect
from .models import CertificationCard
from .forms import CertificationCardForm

def add_certificate(request):
    if request.method == 'POST':
        form = CertificationCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('certificate_list')
    else:
        form = CertificationCardForm()
    return render(request, 'add_certificate.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def certificate_list(request):
    certificates = CertificationCard.objects.all().order_by('-created_at')
    return render(request, 'certificate_list.html', {'certificates': certificates})


def search_certificate(request):
    certificate = None
    searched = False
    card_no = request.GET.get('certificate_no')
    if card_no:
        searched = True
        try:
            certificate = CertificationCard.objects.get(card_no=card_no)
        except CertificationCard.DoesNotExist:
            certificate = None
    return render(request, 'search_certificate.html', {'certificate': certificate, 'searched': searched})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('certificate_list')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')