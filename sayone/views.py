from django.shortcuts import render, HttpResponseRedirect,  redirect, reverse
from django.http import HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView , DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Details , Book
from .forms import LoginForm, RegisterForm , Create_book_form
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, send_mass_mail
import random
from django.core.mail import EmailMessage

# from django.template.loader import get_template_sources

class New_login(View):
    def get(self,request):
        return render(request,'sayone/new_login.html')

# -------------------------sending mail-------------------------------------------------------------
class Send_mail(LoginRequiredMixin,View):
    login_url = '/sayone/login/'
    def get(self,request):
        cur_user = request.user
        print(cur_user.email)
        email = EmailMessage(
            "Testing Mail",
            "Tested successfully :",
            "te4969148@gmail.com",
            ["to1@example.com", "to2@example.com"],
        )
        # message1 = (
        #       "Testing",
        #      "Here is the message",
        #        'mr.prajapatiktn@gmail.com',
        #        ["anurag.prajapatiktn@gmail.com"],
        #    )
        # message2 = (
        #       "Tesing mail",
        #        "Here is another message",
        #        'mr.prajapatiktn@gmail.com',
        #    ["mohammad.o@cisinlabs.com","anurag.pr@cisinlabs.com",'test2@mailinator.com','abc@mailinator.com'],
        # )
        # send_mass_mail((message1,message2), fail_silently=False)
        return redirect("sayone:Index")

# ------------------------------Authentication---------------------------------------------------------
class Logout_user(View):
    def get(self,request):
	    logout(request)
	    return HttpResponseRedirect("/sayone/")
class Login_user(View):
    def get(self,request):
        form = LoginForm()
        message = ''
        return render(request, 'sayone/login.html',context={'form':form,'messages':message})
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.error(request, f'Hello {user.username}! You have been logged in')
                return redirect('sayone:Index')
        else:
            messages.error(request,'Login failed!')

class sign_up(View):
    def post(self,request):
        signup_data = RegisterForm(request.POST)
        if signup_data.is_valid():
            username = signup_data.cleaned_data['username']
            email = signup_data.cleaned_data['email']
            # -----------------------------OTP var ----------------------------
            otp = random.randint(1000,9999)
            send_mail(
                "OTP for registration :",
                f'Hy , your otp is {otp}  ',
                "mr.prajapatiktn@gmail.com",
                [email],
            )
            return render(request,'sayone/email_verify.html')
            # -------------------------------------------------------------
            # signup_data.save()
            # -------------------email sending--------------------------
            print(email)
            send_mail(
                "Testing",
                'Hy  , your account created successfully.  ',
                "mr.prajapatiktn@gmail.com",
                [email],
            )
            # -----------------------------------------------
            return redirect("sayone:login")
        else:
             return render(request, 'sayone/sign_up.html',{'form':signup_data})
    def get(self,request):
        signup_data = RegisterForm()
        return render(request, 'sayone/sign_up.html',{'form':signup_data})
# -------------------------------CRUD UPERATIONS----------------------------------------------------------

class BookList(LoginRequiredMixin,ListView):
    login_url = '/sayone/login/'
    model = Book
    template_name = 'sayone/book_list.html'
    context_object_name = 'book_list'

class BookView(DetailView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'sayone/book_detail.html'
    template_name = 'my_template.html'
    # template_sources = get_template_sources(template_name)
    # for source in template_sources:
    #     print(source)

class BookCreate(CreateView):
    def post(self,request):
        book_data = Create_book_form(request.POST)
        if book_data.is_valid():
            book_data.save()
            current_user = request.user
            send_mail(
                "Book Added",
                'Thankyou for adding book on our plateform, Thanks and Regards  ',
                [current_user.email],
            )
            return redirect('sayone:book_listt')
    def get(self,request):
        book_data = Create_book_form()
        return render(request, 'sayone/book_create.html',{'form':book_data})

class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'Category', 'pages']
    template_name = 'sayone/book_edit.html'
    success_url =  '/sayone/booklist/'

class BookDelete(DeleteView):
    model = Book
    context_object_name = 'd_book'
    template_name = 'sayone/book_delete.html'
    success_url =  '/sayone/booklist/'
# ----------------------------------------------------------------------------------------
class PDF_view(LoginRequiredMixin,TemplateView):
    login_url = '/sayone/login/'
    template_name = 'temp.html'

class Index_view(View):
    def get(self,request):
        return render(request, 'sayone/header.html')


class Details_DetailView(DetailView):
    model = Details
    template_name = 'sayone/details_det.html'
    context_object_name = 'my_details'
    slug_field = 'book_name'
    # ordering = ['book_name']
    # def get_queryset(self):
    #     return Details.objects.filter(is_published='published')

class Details_ListView(LoginRequiredMixin,ListView):
    login_url = '/sayone/login/'
    model = Details
    template_name = 'sayone/details_list.html'
    context_object_name = 'my_details'
    ordering = ['book_name']
    def get_queryset(self):
        return Details.objects.filter(is_published='published')


# class Index_templateview(TemplateView):
#     template_name = 'sayone/header.html'
class Home_view(View):
    def get(self,request):
        return render(request,'sayone/home.html')

class About_templateview(View):
    new_list = ['aaa','bbb','ccc','ddd']
    template_name = 'sayone/about.html'
    def get(self,request):
        return render(request,'sayone/about.html', {'data_list':self.new_list})
