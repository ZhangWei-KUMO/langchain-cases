from django.shortcuts import render
from django.views.generic import View

class Index(View):
    TEMPLATE = 'index.html'
    def get(self, request):
        return render(request, self.TEMPLATE,{'name':"张伟"})