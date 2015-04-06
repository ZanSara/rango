from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm

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
