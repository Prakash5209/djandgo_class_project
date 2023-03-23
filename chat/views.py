from django.shortcuts import render,reverse,get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from chat.models import Message
from chat.forms import ChatForm
from django.http import HttpResponseRedirect

User = get_user_model()

def message_view(request):
    users = User.objects.filter(is_superuser = False).exclude(id = request.user.id)
    context = {'users':users}
    return render(request,"message.html",context)

@login_required
def message_to_user(request,username):
    users = User.objects.filter(is_superuser = False).exclude(id = request.user.id)
    to_user = User.objects.get(username=username)
    messages = Message.objects.filter(
        from_user__in= [request.user,to_user], 
        to_user__in = [request.user,to_user],
        ).order_by('created_at')
    form = ChatForm(request.POST or None)
    if form.is_valid():
        message = form.save(commit=False)
        message.from_user = request.user
        message.to_user = to_user
        message.save()
        return HttpResponseRedirect(reverse('chat:message_user',args = (username, )))
    context = {"conversations":messages,"form":form,"users":users,"username":username}
    return render(request,"message.html",context) 

def delete_message(request):
    messageid = request.POST.get("messageid")
    message = get_object_or_404(Message,id=messageid,from_user = request.user)
    username = message.to_user.username
    message.delete()
    messages.add_message(request,messages.INFO,"your message is been deleted successfully")
    return HttpResponseRedirect(reverse("chat:message_user",args=(username,)))
