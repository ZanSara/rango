from django import forms
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text='Type the category name')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    # Meta is an inline class that provides additional information on the form
    # Here links the ModelForm and its Model

    class Meta:
	model = Category
	fields = ('name',)



class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text='Type the page title')
    url = forms.URLField(max_length=200, help_text='Paste here the page''s URL')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        # If url is not empty and doesn't start with 'http://', adds 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
        return cleaned_data

    class Meta:
	model = Page
	# We can either exclude the category field from the form,
        exclude = ('category',)
        # or specify the fields to include
        #fields = ('title', 'url', 'views')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
	model = User
	fields = ('username', 'email', 'password')
	
class UserProfileForm(forms.ModelForm):
    class Meta:
	model = UserProfile
	fields = ('website', 'picture')
    
