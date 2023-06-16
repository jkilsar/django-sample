from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.views import View

from contacts.models import Contact

class RegisterView(View):

    def get(self, request):
        return render(request, 'accounts/register.html')
    
    def post(self, request):
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if password match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email is being used.")
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, "You are now registered and can login")
                    return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
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
            return redirect('login')

class LogoutView(View):

    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

class DashBoardView(View):

    def get(self, request):
        user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

        context = {
            'contacts': user_contacts
        }

        return render(request, 'accounts/dashboard.html', context)
