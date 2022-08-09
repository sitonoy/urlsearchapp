from django.shortcuts import render
from .forms import InputForm
from .models import Searchlist
from django.views.generic import DeleteView
from django.urls import reverse_lazy


def index(request):

    if request.method == 'POST':
        form = InputForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, "urlsearchapp/result.html")
    else:
        form = InputForm()
        return render(request, 'urlsearchapp/index.html', {'form': form})


def result(request):
    return render(request, 'urlsearchapp/result.html')


def history(request):
    Inputlist = Searchlist.objects.all
    return render(request, 'urlsearchapp/history.html', {'Inputlist': Inputlist})


class ItemDelete(DeleteView):
    template_name = 'urlsearchapp/delete.html'
    model = Searchlist
    success_url = reverse_lazy('history')
