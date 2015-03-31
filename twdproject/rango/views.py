from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template_dict={'boldmessage':'I am from the dictionary'}
    return render(request, 'rango/index.html', template_dict)

def about(request):
    return HttpResponse("""What about Rango?
			\nEveryone *should* know about it. u_u
			<br>
			<br>
			<a href='/rango'>Home</a>
			""")
