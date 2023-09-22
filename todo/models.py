#Importing the required modules
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# This class defines a Profile model which is associated with a User model.
class Profile(models.Model):
    # A OneToOneField relationship is used to extend the User model
    # This ensures that each user can only have one profile
    # If a User is deleted, the associated Profile will also be deleted due to `on_delete=models.CASCADE`.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # This method returns a string representation of the model instance.
    # It returns the username of the associated user.
    def __str__(self):
        return self.user.username

# This class defines a List model which contains a user's to-do items.
class List(models.Model):
    # ForeignKey establishes a many-to-one relationship.
    # This means a user can have multiple lists, but each list is associated with one user.
    # If the associated user is deleted, this list will not be deleted (`on_delete=models.DO_NOTHING`).
    user = models.ForeignKey(User, related_name="lists", on_delete=models.DO_NOTHING)

    # This field contains the main body or text of the to-do item.
    body = models.CharField(max_length=140)

    # This field records when the to-do item was created.
    # `auto_now_add=True` ensures the date is set when the item is first created.
    created_at = models.DateTimeField(auto_now_add=True)

    # This boolean field indicates if the to-do item is completed or not.
    # By default, it is set to False.
    completed = models.BooleanField(default=False)

    # This method returns a string representation of the model instance.
    # It concatenates the user's username, the body of the list, and its creation date.
    def __str__(self):
        return (
            f"{self.user}"          # The associated user's username
            f"{self.body}"          # The body of the list item
            f"({self.created_at:%Y-%m-%d})"   # The creation date in "YYYY-MM-DD" format
        )
