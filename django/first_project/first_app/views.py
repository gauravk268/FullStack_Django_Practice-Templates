from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord

# Create your views here.
def index(request):
    # my_dict = {'insert_me':"now I am coming from first_appviews.py"}
    # return render(request, 'first_app/index.html', context=my_dict)

    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)