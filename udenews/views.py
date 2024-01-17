
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializer import NewsSerializer
from .models import News
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
# from .forms import NewsCreate
from django.views import generic
# Create your views here

# def AddNews(request):
#     add_new_form = NewsCreate()
#     if request.method == 'POST':
#         add_new_form = NewsCreate(data=request.POST)
        
#         if add_new_form.is_valid():
#             add_new_form.save()
            
#             return redirect(reverse('news')+'?ok')
        
#         else:
#             return redirect(reverse('news')+'?error')
        
    
#     return render(request, "udenews/news_form.html", {"form":add_new_form})



class NewsCreate(CreateView):
    model = News
    success_url = reverse_lazy('news-create')
    fields = '__all__'

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    

    