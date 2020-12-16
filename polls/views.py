from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Poll
from . import forms
from django.http import Http404
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
class CreatePoll(generic.CreateView, LoginRequiredMixin):
    model = Poll
    form_class = forms.PollForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class PollList(generic.ListView):
    model = Poll
    template_name = 'polls/poll_list.html'

class UserPollList(generic.ListView, LoginRequiredMixin):
    model = Poll
    template_name = 'polls/user_poll_list.html'

    def get_queryset(self):
        self.poll_user = User.objects.get(username=self.kwargs.get('username'))
        return self.poll_user.polls.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["poll_user"] = self.poll_user 
        return context

class DeletePoll(generic.DeleteView, LoginRequiredMixin):
    model = Poll

    def get_success_url(self):
        return reverse_lazy('polls:user_poll_list', kwargs={'username': self.request.user.username})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Poll Deleted")
        return super().delete(*args, **kwargs)
    

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        selected_option = request.POST.get('inlineRadioOptions')
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            raise Http404
    
        poll.save()
        return redirect('polls:all')
    
    context = {'poll': poll}
    return render(request, 'polls/vote.html', context)

@login_required
def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    context = {'poll': poll}
    return render(request, 'polls/results.html', context)


