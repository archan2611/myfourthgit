from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'doll':'anabelle'}
    return render(request, 'jinja_print.html', d)