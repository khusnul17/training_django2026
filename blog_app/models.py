from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    created_by = models.CharField(max_length=225)
    created_at = models.DateTimeField()
    modified_by = models.CharField(null = True, blank = True)
    modified_at = models.DateTimeField(null = True, blank = True)
    # models.py
#from django.db import models

class Transaksi(models.Model):
    KATEGORI_CHOICES = [
        ('Elektronik', 'Elektronik'),
        ('Aksesoris', 'Aksesoris'),
        ('Furniture', 'Furniture'),
    ]
    
    tanggal = models.DateField()
    produk = models.CharField(max_length=100)
    kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES)
    jumlah = models.IntegerField()
    harga = models.DecimalField(max_digits=12, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-tanggal']
        indexes = [
            models.Index(fields=['-tanggal']),
            models.Index(fields=['kategori']),
        ]
    
    def __str__(self):
        return f"{self.produk} - {self.tanggal}"
