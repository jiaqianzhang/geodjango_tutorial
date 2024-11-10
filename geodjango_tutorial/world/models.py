from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point # create/update a user's profile to include a location

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()
 
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()
 
    # Returns the string representation of the model.
    def __str__(self):
        return self.name
    
# storing a point location on a user's profile
# create profile table 
# make it a 1 to 1 relationship with the user model

# create a field location
# use get user model() for this
User = get_user_model()

# define the profile model by creating a 1 to 1 relationship with the user model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.PointField(null=True, blank=True)
 
    def __str__(self):
        return self.user.username
    
    # function to set user location with user id, latitude and longitude
    def set_user_location(user_id, latitude, longitude):
        user = User.objects.get(id=user_id)
        location = Point(longitude, latitude)  # Point takes (longitude, latitude)
    
        # Create or update the user's profile
        profile, created = Profile.objects.get_or_create(user=user)
        profile.location = location
        profile.save()
    
        return profile