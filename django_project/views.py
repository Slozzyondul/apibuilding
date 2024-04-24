from django.shortcuts import render
import requests
import random


def index(request):
  r1 = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
  res1 = r1.json()
  fact = res1['text']
  #return render(request, 'templates/index.html', {'fact': fact})

  r = requests.get('https://freetestapi.com/api/v1/students')
  students = r.json()
  random_student = random.choice(students)
  name = random_student['name']

  return render(request, 'templates/index.html', {'fact': fact},
                {'name': name})
