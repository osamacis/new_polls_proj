from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse, reverse_lazy
from .models import Choice, Question, Company, Proxy_company
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate  , logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from sayone.views import Index_view
from django.contrib import messages
# Create your views here.

def company(request):
    com_data=Proxy_company.get_company_data.filter().values()
    obj = Proxy_company()
    data = Company.get_company_data.get(id=3)
    data.name='IBM'
    data.save()
    print(data)
    print(com_data)
    domain_name=[]
    def get_domain(data):
        for dic in data:
            print(dic)
            import pdb;
            pdb.set_trace()
            domain_name.append(obj.company_domain(dic['name']))
            print(domain_name)
        return domain_name
    print('ddddfd',get_domain(com_data))
    context={
        'data':com_data,
        # 'domain':get_domain(com_data)
    }
    return render(request,'polls_app/company.html',{'data':com_data})

# @login_required
def index(request):
    latest_question_list = Question.objects.order_by("id")[:3]
    context = {
        "latest_question_list":latest_question_list,
    }
    return render(request, 'polls_app/index.html', context)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    obj = Question()
    pub_dat = list(Question.objects.filter(id=question_id).values('pub_date'))
    print('hhdf',pub_dat[0]['pub_date'])
    context={
        "question": question,
        'was_published_recent':obj.was_published_recently(pub_dat[0]['pub_date'])
    }
    return render(request, "polls_app/details.html", context)



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls_app/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls_app/details.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponsePermanentRedirect(reverse("polls_app:results", args=(question.id,) ))

# def login_user(request):
#     form = LoginForm()
#     message = ''
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 messages.error(request, f'Hello {user.username}! You have been logged in')
#                 return HttpResponseRedirect('/polls_app/')
#         else:
#             messages.error(request,'Login failed!')
#     return render(request, 'polls_app/login.html', context={'form': form, 'messages': message})

# def logout_user(request):
# 	logout(request)
# 	return HttpResponseRedirect("/")
    
# # def sign_up(request):
# #     if request.method == 'POST':
# #         signup_data = UserCreationForm(request.POST)
# #         if signup_data.is_valid():
# #             signup_data.save()
# #             return HttpResponseRedirect('/')
# #     signup_data = UserCreationForm()
# #     return render(request, 'polls_app/signup.html',{'form':signup_data})

# def redirect_to_sayone(request):
#     # return HttpResponseRedirect(reverse("sayone:Index"))
#     return redirect(reverse('sayone:Index'),permanent=True)