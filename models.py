from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User


class UserList(models.Model):
    first_name = models.CharField(max_length=200, blank=True, help_text="The first name of the user.")
    last_name = models.CharField(max_length=200, blank=True, help_text="The last name of the user.")
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        help_text="The email and username of the user. Required."
    )


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class Author(models.Model):
    author = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.author


class Books(models.Model):
    book_name = models.CharField(max_length=50, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    isbn_number = models.IntegerField(unique=True, blank=False, null=False)
    listed = models.BooleanField(default=False)

    def __str__(self):
        return self.book_name


class IssueBook(models.Model):
    book = models.OneToOneField(Books, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now=True)
    return_date = models.DateField()

    def __str__(self):
        return str(self.book) + ' issued to ' + str(self.user)

