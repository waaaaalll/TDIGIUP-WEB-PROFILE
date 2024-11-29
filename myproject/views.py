from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MyProject,GuestBook

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def my_project(request):
    if request.method == "POST":
        nama = request.POST.get("nama")
        alamat = request.POST.get("alamat")
        pesan = request.POST.get("pesan")
        GuestBook.objects.create(nama=nama, alamat=alamat, pesan=pesan)
        return redirect("my_project")  # Redirect untuk mencegah resubmission

    projects = MyProject.objects.all().order_by("-date")  # Mengambil semua data proyek
    guestbooks = GuestBook.objects.all().order_by("-tanggal")  # Data buku tamu terbaru
    return render(request, "my_project.html", {"projects": projects, "guestbooks": guestbooks})