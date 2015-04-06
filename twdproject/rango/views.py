from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    template_context={'categories':category_list}
    return render(request, 'rango/index.html', template_context)

def about(request):
    return HttpResponse("""What about Rango?
			\nEveryone *should* know about it. u_u
			<br>
			<br>
			<a href='/rango'>Home</a>
			""")

def category(request, category_name_slug):
    template_context={}
    try:
	sel_category = Category.objects.get(slug=category_name_slug)
	pages = Page.objects.filter(category=sel_category)
	template_context['category_name'] = sel_category.name
	template_context['category'] = sel_category
	template_context['pages'] = pages
    except Category.DoesNotExist:
	# The template will show a "No such Category": no need to set anything
	pass
    return render(request, 'rango/category.html', template_context)

@login_required
def add_category(request):
    if request.method == 'POST':
	form = CategoryForm(request.POST)
	if form.is_valid():
	    form.save(commit=True)
	    # Call the index view to show the index page
	    return index(request)
	else:
	    # Simply print the errors in the terminal
	    print form.errors
    else:
	form = CategoryForm()
    # Render the form page
    return render(request, 'rango/add_category.html', {'form':form})

@login_required
def add_page(request, category_name_slug):
    try:
	sel_category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
	sel_category = None
    if request.method == 'POST':
	form = PageForm(request.POST)
	if form.is_valid():
	    if sel_category:
		page = form.save(commit=False)
		page.category = sel_category
		page.views = 0
		page.save()
		return category(request, category_name_slug)
	else:
	    print form.errors
    else:
	form = PageForm()
    template_context = {'form':form, 'category':sel_category}
    return render(request, 'rango/add_page.html', template_context)

def register(request):
    registered = False
    if request.method == 'POST':
	user_form = UserForm(data=request.POST)
	profile_form = UserProfileForm(data=request.POST)
	if user_form.is_valid() and profile_form.is_valid():
	    user = user_form.save()
	    #Here we hash the password with set_password()
	    user.set_password(user.password)
	    user.save()
	    # commit=False is used when we need to set the attributes
	    # before writing into the database
	    profile = profile_form.save(commit=False)
	    profile.user = user
	    if 'picture' in request.FILES:
		profile.picture = request.FILES['picture']
	    profile.save()
	    # Registration successful
	    registered = True
	else:
	    print user_form.errors, profile_form.errors
    else:
	user_form = UserForm()
	profile_form = UserProfileForm()
    return render(request, 'rango/register.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})


def user_login(request):
    if request.method == 'POST':
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
	# If the login fails, user = None
	if user:
	    if user.is_active:
		login(request, user)
		return HttpResponseRedirect('/rango/')
	    else:
		return HttpResponse('Your account has been disabled! Sorry...')
	else:
	    print 'Invalid login: {0}, {1}'.format(username, password)
	    return render(request, 'rango/login.html', {error:'Invalid login details. Try again!'})
    else:
	return render(request, 'rango/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rango/')
