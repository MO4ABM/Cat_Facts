# api/views.py
from django.http import JsonResponse
from django.shortcuts import render
import random

cat_facts = [
    r"Cats sleep for about 70% of their lives.",
    r"A group of cats is called a clowder.",
    r"Cats have five toes on their front paws, but only four on their back paws.",
    r"Cats can rotate their ears 180 degrees.",
    r"Each cat's nose is unique, similar to a human fingerprint.",
    r"A cat's purring can have healing properties, lowering stress and promoting healing.",
    r"Cats can jump up to five times their own height in a single leap.",
    r"There are more than 70 million feral cats in the United States.",
    r"Cats have a specialized collarbone that allows them to always land on their feet.",
    r"Domestic cats can run up to 30 miles per hour in short bursts."
]

def get_random_fact():
    return random.choice(cat_facts)

def fact(request):
    fact = get_random_fact()
    return JsonResponse({'fact': fact})

def home(request):
    fact = get_random_fact()
    return render(request, 'home.html', {'fact': fact})
