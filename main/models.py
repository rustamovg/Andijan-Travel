from django.db import models
from ckeditor.fields import RichTextField

# Hotels
class Hotel(models.Model):
  name = models.CharField("Hotel name", max_length=100)
  location = models.CharField("Hotel location", max_length=150)
  google_map = models.CharField("Google map link", max_length=150)
  brief_info = RichTextField()

  def __str__(self):
    return self.name 


class HotelPhoto(models.Model):
  hotel = models.ForeignKey(Hotel, related_name='hotel_photo', on_delete=models.CASCADE)
  photo = models.ImageField("Hotel photo", upload_to="hotel_photos")