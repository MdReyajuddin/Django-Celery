from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.contrib.auth.models import User

from core.forms import GenerateRandomUserForm
from core.tasks import create_random_user_accounts

# Create your views here.
class UsersListView(ListView):
    model = User
    template_name ='user_list.html'

class GenerateRandomUserView(FormView):
    form_class = GenerateRandomUserForm
    template_name = 'generate_random_users.html'

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')



