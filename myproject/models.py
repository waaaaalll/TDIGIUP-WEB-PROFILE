from django.db import models

# Create your models here.
class MyProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='project/images')

    def __str__(self):
        return self.title
    
class GuestBook(models.Model):
    nama = models.CharField(max_length=100)  # Nama pengunjung
    alamat = models.CharField(max_length=255)  # Alamat pengunjung
    pesan = models.TextField()  # Pesan atau komentar dari pengunjung
    tanggal = models.DateTimeField(auto_now_add=True)  # Tanggal input otomatis

    def __str__(self):
        # return f"{self.nama} - {self.tanggal.strftime('%Y-%m-%d')}"
        return f"{self.nama}"