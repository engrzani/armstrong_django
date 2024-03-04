from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import UserProfile, UserAddress
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import pdb

def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            
            # Create a related UserProfile
            UserProfile.objects.create(user=user, contact_number=form.cleaned_data['contact_number'])

            login(request, user)
            return redirect('login')  # Redirect to the home page after successful registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Adjust the redirect URL as needed
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})
  

@login_required
def settings(request):
    user = request.user

    if request.method == 'POST':
        # Handle profile update or address addition logic here
        pass

    return render(request, 'settings.html', {'user': user})
@login_required
def search_armstrong(request):
    armstrong_numbers = []

    if request.method == 'POST':
        min_number = int(request.POST.get('min_number', '0'))
        max_number = int(request.POST.get('max_number', '100000'))
        armstrong_numbers = find_armstrong_numbers(min_number, max_number)

    return render(request, 'search_armstrong.html', {'armstrong_numbers': armstrong_numbers})
@login_required
def find_armstrong_numbers(min_number, max_number):
    # Function to find Armstrong numbers in the specified range
    # Implement your logic here
    # Return a list of Armstrong numbers
    return [num for num in range(min_number, max_number + 1) if is_armstrong(num)]

def is_armstrong(number):
    # Function to check if a number is an Armstrong number
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

    return number == sum_of_digits

from django.shortcuts import render

def check_armstrong(request):
    result = None
    number = None

    if request.method == 'POST':
        number = request.POST.get('number', '')
        result = is_armstrong(int(number))

    return render(request, 'check_armstrong.html', {'result': result, 'number': number})

def is_armstrong(number):
    # Function to check if a number is an Armstrong number
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

    return number == sum_of_digits