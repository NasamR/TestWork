from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import *
from .models import *


def index(request):
    return render(request, 'testwork/index.html')


def for_recruits(request):
    form = Recruit_registration()
    return render(request, 'testwork/for_recruits.html', {'form': form})


def for_siths(request):
    form = Sith_registration()
    answers = Answer.objects.all()
    recruits = Recruit.objects.all()
    return render(request, 'testwork/for_siths.html', {'form': form, 'answers': answers, 'recruits': recruits})


def recruit_registration(request):
    if request.method == 'POST':
        form = Recruit_registration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            planet = form.cleaned_data['planet']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            recruit = Recruit(name=name,
                              planet=Planet.objects.get(name=planet),
                              age=age,
                              email=email)
            if not Recruit.objects.filter(name=name):
                recruit.save()
            else:
                return HttpResponse('This recruit is already exist')
    form = Test_for_recruit()
    questions = Question.objects.filter()
    return render(request, 'testwork/test_for_recruit.html', {'form': form, 'questions': questions, 'name': name})


def test_result(request):
    if request.method == 'POST':
        for question in Question.objects.all():
            answer = request.POST.get(str(question.id))
            username = request.POST.get('username')
            Answer.objects.create(question=question, answer=answer, username=username)
        return HttpResponse('Test is done')


def sith_registration(request):
    if request.method == 'POST':
        form = Sith_registration(request.POST)
        if form.is_valid():
            recruit = form.cleaned_data['recruit']
            sith = form.cleaned_data['sith']
            msg = f'{recruit}, вы приняты!'
            email = Recruit.objects.get(name=recruit)
            send_mail('Тест на Руку Тени',
                      msg,
                      'djangotestwork01@gmail.com',
                      [str(email.email)], fail_silently=True)
    return HttpResponse('Sith registration is done')
