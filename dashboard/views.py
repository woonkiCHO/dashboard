import json
import time

from django.http import HttpResponse
from django.shortcuts import render

from myanalysis.p230 import P230


def home(request):
    data = [];
    for i in range(1, 100):
        person = {};
        person['name'] = 'james' + str(i);
        person['position'] = 'position' + str(i);
        person['office'] = 'office' + str(i);
        person['age'] = i;
        person['salary'] = i * 1000;
        dd = time.time();
        person['date'] = time.ctime(dd);
        data.append(person);

    context = {
        'section':'main_section.html',
        'persons':data
    };
    return render(request, 'index.html',context);

def dashboard1(request):
    context = {
        'section':'dashboard1.html',
    };
    return render(request, 'index.html',context);

def dashboard2(request):
    context = {
        'section':'dashboard2.html',
    };
    return render(request, 'index.html',context);

def dashboard3(request):
    context = {
        'section':'dashboard3.html',
    };
    return render(request, 'index.html',context);

def tabledata(request):
    data = [];
    for i in range(1,100):
        person = {};
        person['name'] = 'james'+str(i);
        person['position'] = 'position' + str(i);
        person['office'] = 'office' + str(i);
        person['age'] =  i;
        person['salary'] = i * 1000;
        dd = time.time();
        person['date'] = time.ctime(dd);
        data.append(person);

    print(data);
    return HttpResponse(json.dumps(data),content_type='application/json');


def chart1(request):
    data = P230().M();
    data.show()
    return HttpResponse(json.dumps(data), content_type='application/json');

def babydashboard(request):
    context = {
        'section': 'babydashboard.html',
    };
    return render(request, 'index.html', context);

def babydashboards(request):
    data = P230().M();
    print(data);
    return HttpResponse(json.dumps(data), content_type='application/json');

def localdashboard(request):
    context = {
        'section':'localdashboard.html',
    };
    return render(request, 'index.html',context);

def localdashboards(request):
    loc = request.GET['location'];
    data = P230().p248(loc);
    print(data);
    return HttpResponse(json.dumps(data), content_type='application/json');
