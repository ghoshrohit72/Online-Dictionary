from django.shortcuts import render
from.models import DictionaryDB
from.forms import DictionaryForm

# Create your views here.
def home(request):

    if request.method=='POST':
        forms = DictionaryForm(request.POST or None)  
        if forms.is_valid():
            forms.save()
            all_letters= DictionaryDB.objects.all().order_by('letter')
            return render (request, 'index.html', {'all_letters': all_letters})

    else:
        all_letters= DictionaryDB.objects.all().order_by('letter')
        return render (request, 'index.html', {'all_letters': all_letters})


def posts(request, pk_test):             #dynamic URLS
    posts = DictionaryDB.objects.get(letter=pk_test)
    return render (request, 'posts.html', {'posts':posts})