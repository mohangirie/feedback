from django.shortcuts import render
from .forms import FeedbackForm
from .models import FeedbackData
import datetime as dt
# Create your views here.
date1= dt.datetime.now()
def Feedback_view(request):
    if request.method== "POST":
        fform=FeedbackForm(request.POST)
        name1= request.POST.get('name' , '')
        rating1= request.POST.get('rating' , '')
        loc1= request.POST.get('loc' , '')
        feedback1= request.POST.get('feedback' , '')
        data= FeedbackData(
            name=name1,
            rating=rating1,
            date=date1,
            loc=loc1,
            feedback=feedback1,
        )
        data.save()
        fform=FeedbackForm()
        feedbacks= FeedbackData.objects.all()
        return render(request,'fform.html',{'fform':fform,'feedbacks':feedbacks})
    else:
        fform = FeedbackForm()
        feedbacks= FeedbackData.objects.all()
        return render(request, 'fform.html', {'fform': fform,'feedbacks':feedbacks})
