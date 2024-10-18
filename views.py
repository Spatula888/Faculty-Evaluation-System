from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Faculty, Evaluation
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        password = request.POST.get('password')

        # Dictionary mapping roles to usernames
        role_based_usernames = {
            'admin': 'admin_username',
            'student': 'student_username',
            'faculty': 'faculty_username',
        }

        # Get the username based on the selected role
        username = role_based_usernames.get(role)

        if username:
            # Authenticate the user with the role-based username
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect based on role
                if role == 'admin':
                    return redirect('home')
                elif role == 'student':
                    return redirect('student_dashboard')
                elif role == 'faculty':
                    return redirect('faculty_dashboard')
            else:
                messages.error(request, 'Invalid credentials.')
        else:
            messages.error(request, 'Invalid role selected.')

    return render(request, 'login.html')


def faculty_login_view(request):
    return render(request, 'faculty-login.html')
def home_view(request):
    return render(request, 'home.html')

def evaluation_list(request):
    evaluations = Evaluation.objects.all()  # Retrieve all evaluations
    return render(request, 'evaluation_list.html', {'evaluations': evaluations})

def register_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Define role-based usernames
        role_based_usernames = {
            'admin': 'admin_username',  # Replace with actual admin username
            'student': 'student_username',  # Replace with actual student username
            'faculty': 'faculty_username',  # Replace with actual faculty username
        }

        # Get the username based on the selected role
        username = role_based_usernames.get(role)

       def register_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')  # Get role from form
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # Dictionary to map roles to default usernames
        role_based_usernames = {
            'admin': 'admin_username',
            'student': 'student_username',
            'faculty': 'faculty_username',
        }

        # Generate username based on role
        username = role_based_usernames.get(role)

        if username and password == password_confirm:
            try:
                # Create a user with role as the username
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'Error: {str(e)}')
        else:
            messages.error(request, 'Passwords do not match or invalid role selected.')

    return render(request, 'register.html')
