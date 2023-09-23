from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth 
from django.contrib import messages
from .models import Profile,List
from django.contrib.auth.decorators import login_required
# Create your views here.

# The dashboard view, which is protected by the login_required decorator.
# If a user is not logged in, they'll be redirected to the 'login' view.
@login_required(login_url='login')
def dashboard(request):
    # If the request is a POST request (e.g., submitting a form)
    if request.method == "POST":
        # Checking if the user is logged in
        if request.user is not None:
            list_name = request.POST['list_name']

            # Creating a new List object
            list = List(body=list_name)
            list.user = request.user
            list.save()
            
            # Informing the user that the task was added successfully
            messages.info(request, "Your Task Was Added Successfully")
            return redirect('/')
        else:
            return redirect('/')
    else:
        # Fetching the count of uncompleted tasks for the logged-in user
        uncompleted_task_count = List.objects.filter(user=request.user, completed=False).count()
        
        # Rendering the dashboard page with the uncompleted task count
        return render(request, "dashboard.html", {"uncompleted_task_count": uncompleted_task_count})


# User registration view.
def register(request):
    # Check if the request method is POST, which implies the form is being submitted.
    if request.method == "POST":
        # Retrieve data from the registration form.
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']  # Confirmation password.

        # Check if both entered passwords match.
        if password == password2:
            # Check if a user with the given email already exists.
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect("register")
            # Check if a user with the given username already exists.
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Used")
                return redirect("register")
            else:
                # If the email and username are both unique, create a new user.
                user = User.objects.create_user(username=username, email=email, password=password)

                # Fetch the created user
                new_model = User.objects.get(username=username)
                
                # Create a profile for the newly registered user.
                create_profile = Profile.objects.create(user=new_model)
                create_profile.save()
                
                # Redirect the user to a success page after successful registration.
                return render(request, 'success.html', {"new_model": new_model})
        else:
            # If the passwords do not match, inform the user.
            messages.info(request, "Password Not The Same")
            return redirect("register")
    # If the request method is not POST (i.e., it's a GET request or any other HTTP method), 
    # then render the registration form for the user to fill out and submit.
    else:
        return render(request, "register.html")

  
# This function handles the user login process.
def login(request):
    # Check if the incoming request is a POST (i.e., the form is being submitted).
    if request.method == "POST":
        # Retrieve the submitted username and password from the form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's built-in authenticate method to validate the provided credentials.
        user = auth.authenticate(username=username, password=password)

        # If the authentication is successful and a user object is returned.
        if user is not None:
            # Log the user in using Django's built-in login method.
            auth.login(request, user)
            # Redirect to the homepage after successful login.
            return redirect('/')
        else:
            # If authentication fails, display an error message.
            messages.info(request, "Credentials Invalid")
            # Redirect back to the login page to let the user try again.
            return redirect("login")
    # If the request is not a POST (e.g., a GET request to view the login page).
    else:
        # Render the login page template.
        return render(request, "login.html")


# This function marks a specific task as completed.
def finish(request, list_id):
    # Retrieve the task item using the provided list_id from the database.
    item = List.objects.get(pk=list_id)
    # Set the 'completed' attribute of the task item to True.
    item.completed = True
    # Save the changes made to the task item in the database.
    item.save()
    # Redirect the user to the homepage after the operation.
    return redirect('/')

# This function marks a specific task as uncompleted or pending.
def unfinish(request, list_id):
    # Retrieve the task item using the provided list_id from the database.
    item = List.objects.get(pk=list_id)
    # Set the 'completed' attribute of the task item to False.
    item.completed = False
    # Save the changes made to the task item in the database.
    item.save()
    # Redirect the user to the homepage after the operation.
    return redirect('/')

# This function deletes a specific task from the database.
def delete(request, list_id):
    # Retrieve the task item using the provided list_id from the database.
    list = List.objects.get(id=list_id)
    # Delete the retrieved task item from the database.
    list.delete()
    # Redirect the user to the homepage after the operation.
    return redirect('/')


        