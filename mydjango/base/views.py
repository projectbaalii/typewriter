# from django.shortcuts import render
# from .models import BlogPost
# from .forms import BlogPostForm  # Assuming you're using a form for handling the BlogPost creation

# def create_blog_post(request):
#     if request.method == "POST":
#         form = BlogPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('blog_list')  # Redirect to a list or success page after saving
#     else:
#         form = BlogPostForm()

#     return render(request, 'create_blog_post.html', {'form': form})
from django.shortcuts import render
from .models import BlogPost

def blog_list(request):
    blog_posts = BlogPost.objects.all()  # Fetch all blog posts from the database
    return render(request, 'blog_list.html', {'blog_posts': blog_posts})



