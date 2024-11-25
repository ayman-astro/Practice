from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album


# Create your views here.
def add_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_album")
    else:
        form = AlbumForm()
    return render(request, "add_album.html", {"form": form})


def edit_album(request, id):
    album = Album.objects.get(id=id)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = AlbumForm(instance=album)
    return render(request, "add_album.html", {"form": form})
