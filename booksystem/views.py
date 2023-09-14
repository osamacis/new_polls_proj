from django.shortcuts import render
from django.views import View
# Create your views here.

class Header(View):
    def get(self,request):
        return render(request, 'booksystem/header.html')