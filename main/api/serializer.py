from rest_framework import serializers
from main.models import Hotel, HotelPhoto

class HotelPhotoSerializer(serializers.ModelSerializer):
  photo_url = serializers.SerializerMethodField()
  class Meta:
    model = HotelPhoto
    fields = ['photo_url']

  def get_photo_url(self, hotels):
    request = self.context.get('request')
    photo_url = hotels.photo.url
    return request.build_absolute_uri(photo_url)
    

class HotelSerializer(serializers.ModelSerializer):
  hotel_photo = HotelPhotoSerializer(many=True, read_only=True)
  class Meta:
    model = Hotel
    fields = ['name', 'location', 'google_map', 'brief_info', 'hotel_photo']