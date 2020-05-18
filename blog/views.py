from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request):
    blog = Blog.objects
    blog = blog.reverse()
    context = {
    'blog':blog,
    }
    return render(request,'blog/blog.html',context )
