# Importing necessary modules and views.
from .import views
from django.urls import path
from django.contrib.auth import views as auth_views  # Importing Django's built-in authentication views.

# This list defines the URL patterns for the application.
urlpatterns = [
    # This pattern maps the root URL to the dashboard view.
    path("", views.dashboard, name="dashboard"),

    # This pattern maps the "register" URL to the register view.
    path("register", views.register, name="register"),

    # This pattern maps the "login" URL to the login view.
    path("login", views.login, name="login"),

    # This pattern maps the "logout" URL to Django's built-in LogoutView.
    # Upon logging out, the user will be presented with the "logged_out.html" template.
    path("logout", auth_views.LogoutView.as_view(template_name="logged_out.html"), name="logout"),

    # This pattern maps a URL with a specific list_id to the finish view.
    # It's used to mark a list item as finished or "crossed off".
    path("cross_off/<list_id>", views.finish, name='finish'),

    # This pattern maps a URL with a specific list_id to the unfinish view.
    # It's used to mark a list item as unfinished or "uncrossed".
    path("uncross/<list_id>", views.unfinish, name='unfinish'),

    # This pattern maps a URL with a specific list_id to the delete view.
    # It's used to delete a list item.
    path("delete/<list_id>", views.delete, name='delete'),
]
