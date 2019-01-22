import random
from django.shortcuts import render, HttpResponse, reverse
from django.views.generic import *
from .models import Question, Test, FeedbackForm

def CreateTest(request):
    questions = []

    for unit in range(1,6):
        temp_question = Question.objects.filter(chapter=unit)
        picked_question_index = random.sample(range(0, len(temp_question)), 10)
        opt = []

        for x in picked_question_index:
            questions.append(temp_question[x])
            opt = [questions[-1].optionA, questions[-1].optionB,
                questions[-1].optionC, questions[-1].optionD]
            random.shuffle(opt)
            questions[-1].optionA = opt[0]
            questions[-1].optionB = opt[1]
            questions[-1].optionC = opt[2]
            questions[-1].optionD = opt[3]

    random.shuffle(questions)
    return render(request, 'exam/base.html', {'questions':questions})

def SubmitTest(request):
    temp = Test.objects.create(id=request.POST['roll'])
    temp.name = request.POST['name']
    request.session['id'] = request.POST['roll']
    score = 0
    tot = 0
    k = 0
    temp.question = ""
    temp.answer = ""
    for x in request.POST:
        if(x.isnumeric()):
            tot += 1
            temp.question+=str(x)+","
            temp.answer+=request.POST[x]+", "
            if(Question.objects.get(pk=x).answer_text == request.POST[x]):
                score += 1

    temp.score = score
    temp.save()
    return HttpResponse("""<center><h3><br><br>The test is over</h3><br><br><br>
    <h1><a href="{}">Click here for feedback form</a></h1></center>""".format(reverse('exam:Feedback')))

def Feedback(request):
    return render(request, 'exam/feedback.html', {});

def TestOver(request):
    temp = FeedbackForm.objects.create(id=int(request.session['id']))
    temp.f1 = request.POST['q1']
    temp.f2 = request.POST['q2']
    temp.f3 = request.POST['q3']
    temp.f4 = request.POST['q4']
    temp.f5 = request.POST['q5']
    temp.save()

    score = Test.objects.get(id=int(request.session['id'])).score
    return HttpResponse("<center><h3><br><br>Thanks for feedback</h3><br><br><br><h1>Your Score in thoery test is {} out of {}</h1></center>".format(score, 40))
