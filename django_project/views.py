from django.shortcuts import render
import requests
import random


def index(request):
  r1 = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
  res1 = r1.json()
  fact = res1['text']
  return render(request, 'templates/index.html', {'fact': fact})


def news(request):
  r2 = request('')
  res2 = r2.json()
  news = res2['text']
  return render(request, 'templates/news.html', {'news': news})


def sports(request):
  r3 = request('')
  res3 = r3.json()
  sports = res3['text']
  return render(request, 'templates/sports.html', {'sports': sports})


def images(request):
  r4 = request('')
  res4 = r4.json()
  images = res4['text']
  return render(request, 'templates/images.html', {'images': images})


