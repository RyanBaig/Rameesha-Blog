from django.shortcuts import render, get_object_or_404
from .models import Blogpost

# Create your views here.
def index(request):
    myposts = Blogpost.objects.all()
    # get the most recent 4 posts
    recent_posts = myposts[::-1][:4]
    return render(request, "blog/index.html", {'myposts': myposts, 'recent_posts': recent_posts})

def blogpost(request, id):
    # EXERCISE COMPLETED (ADD NEXT/PREVIOUS BUTTONS FOR POSTS)
    post = get_object_or_404(Blogpost, post_id=id)
    next_post = Blogpost.objects.filter(post_id=id + 1).first()
    prev_post = Blogpost.objects.filter(post_id=id - 1).first()

    # Check if next_post and prev_post exist
    if not next_post:
        next_post = "No New Posts..."
    if not prev_post:
        prev_post = "No Previous Posts..."

    return render(request, "blog/blogpost.html", {'post': post, 'next_post': next_post, 'prev_post': prev_post})


def searchMatch(query, item):
    if (
        query.lower() in item.title.lower()
        or query in item.first_head.lower()
    ):
        return True
    else:
        return False


def search(request):
    query = request.GET.get("q")
    if query or query != "":
        # Retrieve all blog posts from the database
        all_blog_posts = Blogpost.objects.all()

        # Filter blog posts based on searchMatch function
        results = [post for post in all_blog_posts if searchMatch(query, post)]

        # Pass the results to the template
        return render(request, "blog/search.html", {"results": results, "query": query})
    else:
        # If no query is provided, render a basic search page
        return render(request, "blog/search.html")
