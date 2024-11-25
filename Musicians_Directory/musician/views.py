from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import Musician
from album.models import Album


# create your views here.
def add_musician(request):
    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_musician")
    else:
        form = MusicianForm()
    return render(request, "add_musician.html", {"form": form})


def edit_musician(request, id):
    musician = Musician.objects.get(id=id)
    if request.method == "POST":
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = MusicianForm(instance=musician)
    return render(request, "add_musician.html", {"form": form})


def delete_musician(request, id):
    musician = Musician.objects.get(id=id)
    musician.delete()
    return redirect("homepage")
