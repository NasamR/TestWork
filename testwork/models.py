from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recruit(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet, on_delete=models.DO_NOTHING)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Sith(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=20)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.answer
