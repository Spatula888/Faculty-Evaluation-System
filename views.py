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

        # Define role-based usernames
        role_based_usernames = {
            'admin': 'admin_username',  # Replace with actual admin username
            'student': 'student_username',  # Replace with actual student username
            'faculty': 'faculty_username',  # Replace with actual faculty username
        }

        # Get the username based on the selected role
        username = role_based_usernames.get(role)

        if username:  # Check if the role is valid
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect based on role
                if role == 'admin':
                    return redirect('admin_dashboard')
                elif role == 'student':
                    return redirect('student_dashboard')
                elif role == 'faculty':
                    return redirect('faculty_dashboard')
            else:
                return render(request, 'home.html', {'error': 'Invalid credentials.'})
        else:
            return render(request, 'home.html', {'error': 'Invalid role selected.'})

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

        if username and password == password_confirm:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('login')  # Redirect to the login page after successful registration
            except Exception as e:
                messages.error(request, f'Error: {str(e)}')
        else:
            if not username:
                messages.error(request, 'Invalid role selected.')
            else:
                messages.error(request, 'Passwords do not match.')

    return render(request, 'register.html')