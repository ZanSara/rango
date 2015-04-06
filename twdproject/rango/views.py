from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

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
	
