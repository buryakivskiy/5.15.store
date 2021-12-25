from django.shortcuts import render,redirect
from .forms import FeedBackForm
from django.views.generic import View
from django.contrib import messages


class FeedBackView(View):
    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, settings.MY_INFO, "Сейчас перезвоним!")
        else:
            messages.add_message(request, settings.MY_INFO, "Заполните обязательные поля!")
        return redirect("/")