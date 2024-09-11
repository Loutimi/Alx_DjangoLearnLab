from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserChangeForm, CommentForm
from .models import Post, Comment, Tag

from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import UserPassesTestMixin

from django.urls import reverse
from django.db.models import Q

class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = "blog/register.html"
    template_name_suffix = 'form'
    success_url = '/profile'


class Login(LoginView):
    template_name = 'blog/login.html'


@login_required
def ProfileView(request):
    user = request.user

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            redirect('profile')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, "blog/profile.html", {'form': form})


# class Logout(LogoutView):
#     template_name = 'blog/logout.html'

class NewPost(CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = '__all__'
    success_url = "/posts"


class Posts(ListView):
    model = Post
    template_name = "blog/post_list.html"


class PostDetail(DetailView):
    model = Post
    template_name = "blog/posts_detail.html"


class PostEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/update_post.html"
    fields = '__all__'
    success_url = "/posts"

    def handle_no_permission(self):
        return redirect('login')


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = "/posts"

    def handle_no_permission(self):
        return redirect('login')
    

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.post = get_object_or_404(Post, pk=kwargs['post_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.post = self.post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'post_id':self.post.id})

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.post = get_object_or_404(Post, pk=kwargs['post_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Comment.objects.filter(post=self.post)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'post_id': self.post.id})

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_queryset(self):
        return Comment.objects.filter(post=self.post)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'post_id': self.post.id})


class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list_by_tag.html'

def search(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        )
    else:
        posts = Post.objects.all()
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})



    
