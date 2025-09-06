from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  mymembers = Member.objects.all().values()
  mydata = Member.objects.all()
  mydata2 = Member.objects.values_list('firstname', flat = True)
  mydata3 = Member.objects.filter(firstname='Juana').values()
  mydata4 = Member.objects.filter(lastname='Perez', id=4).values()
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    'firstname': 'Linus',
    'mymembers': mymembers,
    'mymembers2': mydata,
    'mymembers3': mydata2,
    'mymembers4': mydata3,
    'mymembers5': mydata4,
    'greeting': 0,
    'x': ['Apple', 'Banana', 'Cherry'],
    'y': ['Apple', 'Banana', 'Cherry'],
    'cars': [
      {
        'brand': 'chevrolet',
        'model': 'corsa',
        'year': 2011
      },
      {
        'brand': 'ford',
        'model': 'explorer',
        'year': 2024
      },
      {
        'brand': 'chery',
        'model': 'evolution',
        'year': 2017
      },
    ]
  }
  return HttpResponse(template.render(context, request))