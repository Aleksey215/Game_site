from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# ограничение доступа к странице с профилем (только для зарегистрированных)
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'
