from django.db import models

class movieDetails(models.Model):
    movieName = models.CharField(max_length=50)
    cinemaTheatre = models.CharField(max_length=100)
    showTime = models.CharField(max_length=50)
    patronName = models.CharField(max_length=50)
    mobileNo = models.CharField(max_length=50)
    seatNo = models.CharField(max_length=50)
    seatSeries = models.CharField(max_length=10)
    movieDate = models.CharField(max_length=30)
