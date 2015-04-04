from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    template_dict={'categories':category_list}
    return render(request, 'rango/index.html', template_dict)

def about(request):
    return HttpResponse("""What about Rango?
			\nEveryone *should* know about it. u_u
			<br>
			<br>
			<a href='/rango'>Home</a>
			""")
