from django.shortcuts import render

# Create your views here.
def jinja1(request):
    d={'name': 'archan', 'age': 23}
    return render(request, 'jinja1.html',d)