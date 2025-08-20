# This file is to demonstrate that the shell commands have been executed

# Shell Tutorial 2: Playing with the API

from polls.models import Question, Choice
from django.utils import timezone

Question.objects.all()
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id
q.question_text
q.pub_date
q.question_text = "What's up?"
q.save()
Question.objects.all()  
Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith="What")
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)
Question.objects.get(id=2)
Question.objects.get(pk=1)
q = Question.objects.get(pk=1)
q.was_published_recently()
q = Question.objects.get(pk=1)
q.choice_set.all()
q.choice_set.create(choice_text="Not much", votes=0)
q.choice_set.create(choice_text="The sky", votes=0)
c = q.choice_set.create(choice_text="Just hacking again", votes=0)
c.question
q.choice_set.all()
q.choice_set.count()
Choice.objects.filter(question__pub_date__year=current_year)
c = q.choice_set.filter(choice_text__startswith="Just hacking")
c.delete()

# Shell Tutorial 5
import datetime
from django.utils import timezone
future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
future_question.was_published_recently()

from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import Client
client = Client()
response = client.get("/")
response.status_code
from django.urls import reverse
response = client.get(reverse("polls:index"))
response.status_code
response.content
response.context["latest_question_list"]