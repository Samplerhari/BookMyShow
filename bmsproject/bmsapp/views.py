from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import movieDetails
def bmsapp(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render({},request))
def myTicket(request):
    myallDataList = movieDetails.objects.all().values()
    template = loader.get_template('MyTicket.html')
    context = {
        'myallDataList': myallDataList
    }
    return HttpResponse(template.render(context, request))

def contactUs(request):
    template=loader.get_template('ContactUs.html')
    return HttpResponse(template.render({},request))


def saveMovieData(request):
    aaa = request.POST['movieName']
    bbb = request.POST['cinemaTheatre']
    ccc = request.POST['showTime']
    ddd = request.POST['mobileNo']
    eee = request.POST['seatSeries']
    fff = request.POST['seatNo']
    ggg = request.POST['movieDate']
    ppp = request.POST['patronName']
    hhh = movieDetails(patronName=ppp,movieName=aaa,cinemaTheatre=bbb,showTime=ccc,mobileNo=ddd,seatSeries=eee,seatNo=fff,movieDate=ggg)
    hhh.save()
    return HttpResponseRedirect(reverse('myTicket'))

def updateBooking(request,id):
    mydata=movieDetails.objects.get(id=id)
    template=loader.get_template('UpdateMyTicket.html')
    context={
        'mydata':mydata
    }
    return HttpResponse(template.render(context,request))

def updateBookingData(request,id):
    aaa = request.POST['movieName']
    bbb = request.POST['cinemaTheatre']
    ccc = request.POST['showTime']
    ddd = request.POST['mobileNo']
    eee = request.POST['seatSeries']
    fff = request.POST['seatNo']
    ggg = request.POST['movieDate']
    ppp = request.POST['patronName']
    newdata=movieDetails.objects.get(id=id)
    newdata.patronName=ppp
    newdata.movieName=aaa
    newdata.cinemaTheatre=bbb
    newdata.showTime=ccc
    newdata.mobileNo=ddd
    newdata.seatSeries=eee
    newdata.seatNo=fff
    newdata.movieDate=ggg
    newdata.save()
    return HttpResponseRedirect(reverse(myTicket))

def deleteBooking(request,id):
    mydata = movieDetails.objects.get(id=id)
    mydata.delete()
    return HttpResponseRedirect(reverse('myTicket'))
