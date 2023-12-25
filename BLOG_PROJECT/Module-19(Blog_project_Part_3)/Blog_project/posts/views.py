from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
from .import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView,DetailView
# Create your views here.


@login_required
def add_post(request):
    if request.method == "POST":
        post_form = forms.Post(request.POST)
        if post_form.is_valid():
            # post_form.cleaned_data['author'] = request.user
            post_form.instance.author = request.user
            post_form.save()
            return redirect('add_post')

    else:
        post_form = forms.Post()
    return render(request, 'post.html', {'poost': post_form})


# Add_Post Using class based view
method_decorator(login_required, name="dispatch")
class createview(CreateView):
    model = models.post
    form_class = forms.Post
    template_name = 'post.html'
    success_url = reverse_lazy('add_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def edit_post(request, id):
    post = models.post.objects.get(pk=id)
    post_form = forms.Post(instance=post)
    # print(post.title)
    if request.method == 'POST':  # user post request koreche
        # user er post request data ekhane capture korlam
        post_form = forms.Post(request.POST, instance=post)
        if post_form.is_valid():
            # post kora data gula amra valid kina check kortechi
            post_form.instance.author = request.user
            post_form.save()  # jodi data valid hoy taile database e save korbo
            # sob thik thakle take add author ei url e pathiye dibo
            return redirect('home')
    return render(request, 'post.html', {'poost': post_form})


# Edit_Post Using class based view
method_decorator(login_required, name="dispatch")
class EditPostView(UpdateView):
    model = models.post
    form_class = forms.Post
    template_name = 'post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


@login_required
def delete_post(request, id):
    post = models.post.objects.get(pk=id)
    post.delete()
    return redirect('home')


# Delete_Post Using class based view
method_decorator(login_required, name="dispatch")
class DeletePostView(DeleteView):
    model = models.post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'



class DetailPostView(DetailView):
    model = models.post
    pk_url_kwarg ='id'
    template_name = 'post_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

