from django.shortcuts import render, get_object_or_404
from django.views import View

from main.models import Post, Category


class PostsList(View):
    def get(self, request):
        posts = Post.objects.all()
        q = request.GET.get("q")
        if q:
            posts = posts.filter(title__icontains=q)
        template_name = "posts.html"
        return render(request, template_name, context={"posts": posts})


class CategoryDetails(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, slug=category_id)
        posts = category.posts.all()
        template_name = "category.html"
        return render(request, template_name, context={"category": category, "posts": posts})
