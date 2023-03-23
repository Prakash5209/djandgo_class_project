from django.shortcuts import render,reverse,get_object_or_404
from post.models import Post,Status,Like
from post.forms import PostForm,CommentForm
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


def home(request):
    posts = Post.objects.filter(status=Status.PUBLIC).order_by("-created_at")
    context = {'posts':posts}
    return render(request,'home.html',context)

@login_required
def create_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        messages.add_message(request,messages.INFO,'your post created successfully!')
        return HttpResponseRedirect(reverse('post:home'))
    context = {'form':form}
    return render(request,"post.html",context)

@login_required
def edit_post(request,postid):
    # try:
    #     post = Post.objects.get(id=postid)
    # except Post.DoesNotExist:
    #     raise Http404()
    post = get_object_or_404(Post,id=postid,user=request.user)
    form = PostForm(request.POST or None,instance=post)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        messages.add_message(request,messages.INFO,'your post updated sucessfully!')
        return HttpResponseRedirect(reverse('post:home'))
    context = {'form':form}
    return render(request,'post.html',context)

@login_required
def delete_post(request):
    postid = request.POST.get('postid')
    post = get_object_or_404(Post,id = postid,user=request.user)
    post.delete()
    messages.add_message(request,messages.INFO,'your post removed successfull')
    return HttpResponseRedirect(reverse('post:home'))

@login_required
def like_post(request,postid):
    post = get_object_or_404(Post,id = postid)
    user = request.user
    like,created = Like.objects.get_or_create(post = post,user = user)
    if not created:
        if like.is_liked:
            like.is_liked = False
        else:
            like.is_liked = True
        like.save()
    total = send_mail("post liked",f"your post: {post.description} has been likes.","prakashkchaudhary5209@gmail.com",[user.email])
    print(total)
    total_likes = post.likes.filter(is_liked = True).count()
    return JsonResponse({"likes":total_likes},safe = False)

@login_required
def comment_post(request,postid):
    post = get_object_or_404(Post,id = postid)
    comments = post.comments.all()
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return HttpResponseRedirect(reverse('post:comment_post', args = (postid,)))
    context = {'post':post,'comments':comments,'form':form}
    return render(request,'post_comments.html',context)

