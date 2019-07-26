from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'blog/index.html')

def blog_list(request):
    return render(request,'blog/list.html')

def blog_detail(request):
    return render(request,'blog/detail.html')