#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("""Rango says Hello World!
			<br>
			<br>
			<a href='/rango/about'>About</a>
			""")

def about(request):
    return HttpResponse("""What about Rango?
			\nEveryone *should* know about it. u_u
			<br>
			<br>
			<a href='/rango'>Home</a>
			""")
