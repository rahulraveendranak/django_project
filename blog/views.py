from django.shortcuts import render

posts = [
    {
        'author':'Rahul',
        'title':'blog post 1',
        'content':'first post content',
        'date_posted':'August 27,2018'
    },
    {
       'author':'Ram',
        'title':'blog post 2',
        'content':'second post content',
        'date_posted':'August 27,2018' 
    }
]

# Create your views here.

def home(request):
    context ={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title': about})