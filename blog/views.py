from django.shortcuts import render,redirect

from .models import Post
from .forms import PostForm


def home(request):
    posts=Post.objects.all
    return render(request,'index.html',{'posts':posts})

def createPostView(request):
    if request.method == "POST":
        form = PostForm(request.POST) #to get the data posted
        if form.is_valid():
            post = form.save(commit=False) #commit=false ensures the data is not saved in database but returned as a post object
            post.author = request.user #sets the author to current logged in user
            post.save() #saves the modified object having the author field as current logged in user
            return redirect('home')

    else:
        form = PostForm()

    return render(request, 'add.html', {'form': form})


