# coding: UTF-8
from django.shortcuts import render
from const.forms import InventoryTypeForm
from django.template import RequestContext
from django.views.decorators import csrf
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect,HttpResponse
import json
from django.db import transaction

from news.forms import NewsForm
from news.models import News, DocumentFile, NewsCategory

def userManagementViews(request):
    """
    JunHU
    """
    context = {}
    return render(request, "management/user_management.html", context)

def groupManagementViews(request):
    """
    JunHU
    """
    context = {}
    return render(request, "management/group_management.html", context)

def titleManagementViews(request):
    """
    JunHU
    """
    context = {}
    return render(request, "management/title_management.html", context)

def messageManagementViews(request):
    """
    JunHU
    """
    context = {}
    return render(request, "management/message_management.html", context)



def newsReleaseViews(request):
    """
    mxl
    """
    if request.method == 'POST':
        files = request.FILES.getlist("myfiles")
        newsform = NewsForm(request.POST)
        if newsform.isvalid():
            news_news = News(news_title = newsform.cleaned_data["news_title"],
                             news_content = newsform.cleaned_data["news_content"],
                             news_date = newsform.cleaned_data["news_date"],
                             news_category = NewsCategory.objects.get(id = newsform.cleaned_data["news_category"])
                            )
            news_news.save()
            for f in files:
                doc = DocumentFile(f, news_news)
                doc.save()
    else:
        newsform = NewsForm()
        context = {
            'newsform' : newsform
        }
        return render(request, "management/news_release.html", context)