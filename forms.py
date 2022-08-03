from django import forms
#from .models import UserProfile
from .models import Books, Author, Category, IssueBook
from django.contrib.auth.forms import UserCreationForm, User, UserChangeForm, PasswordChangeForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['type'] = 'password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['type'] = 'password'


class EdithProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','date_joined', ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'date_joined': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }




class PasswordChangeForms(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),}


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('author',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('book_name','author','price','category','isbn_number')

        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'isbn_number': forms.TextInput(attrs={'class': 'form-control'}),

        }

class IssueForm(forms.ModelForm):
    class Meta:
        model = IssueBook
        fields = ('book', 'user', 'return_date',)

        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'return_date': forms.DateInput(attrs={'class': 'form-control'}),

        }