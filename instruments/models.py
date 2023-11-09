from django.db import models

class Instrument(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    instrument_type = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='instrument_photos/')

    def __str__(self):
        return f"{self.name} ({self.instrument_type}) - ${self.price}"

class Order(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.instrument.price * self.quantity
