from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from contacts.models import Contact

from .forms import CreateUserForm

class RegisterView(View):

    def get(self, request):
        form = CreateUserForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/registerform.html', context)
    
    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You are now registered and can login")
            return redirect('two_factor:login')
        else:
            messages.error(request, form.errors.as_text())
            return redirect('register')


class LoginView(View):

    def get(self, request):
        return render(request, 'accounts/login.html')
    
    def post(self, request):
        # Get form values
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('two_factor:login')

class LogoutView(View):

    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

class DashBoardView(LoginRequiredMixin, View):

    def get(self, request):
        user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

        context = {
            'contacts': user_contacts
        }

        return render(request, 'accounts/dashboard.html', context)
