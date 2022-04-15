from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required       #


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
#                 "edit": edit,
#                 "delete": delete,
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))



@login_required(login_url='login')
def update_comment(request,pk):
    comment=Comment.objects.get(id=pk)
    form=CommentForm(instance=comment)  #whi form huga bs usko edit krsktay hungay 
    context={'form':form}

    if request.method=='POST':
        form=CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request,'update_comment.html',context)

@login_required(login_url='login')
def delete(request,pk):
    item=Comment.objects.get(id=pk)
    # todoItem=str(item).split(',')[1].split(':')[1][2:-2]
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context={
        # 'item':todoItem
    }
    return render(request,'delete.html',context)
