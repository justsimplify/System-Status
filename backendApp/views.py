import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from utils.helpers import Protocol, check_connectivity
from utils.producer import produce
from utils.specification import Specification

from .models import Specs


def parse_data(json_data):
    print(json_data)
    return Specification.from_json(json.dumps(json_data))


def insert_model(data: Specification):
    try:
        r = Specs(name=data.name, description=data.description, pingUrl=data.pingUrl,
                  interval=data.interval, waitTime=data.waitTime).save()
        return r
    except Exception as e:
        return str(e)


def fetch_data():
    return Specs.objects.all()


def fetch_data_by_key(pk):
    return Specs.objects.get(pk=pk)


def parse_spec_object(s: Specs):
    r = [{'name': v.name, 'description': v.description, 'pingUrl': v.pingUrl,
          'waitTime': v.waitTime, 'interval': v.interval, 'status': v.status, 'pk': str(v.pk)} for v in s]
    return r


def parse_spec_object_by_key(v: Specs):
    return {'name': v.name, 'description': v.description, 'pingUrl': v.pingUrl,
            'waitTime': v.waitTime, 'interval': v.interval, 'status': v.status, 'pk': str(v.pk)}


@csrf_exempt
def index(request, uri=None, timeout=5):
    if request.method == 'GET':
        r = check_connectivity(Protocol.HTTP, uri, timeout)
        return HttpResponse(r)
    elif request.method == 'POST':
        data: Specification = parse_data(json.loads(request.body))
        res = insert_model(data)
        return HttpResponse(repr(res))


@csrf_exempt
def get_data(request):
    if request.method == 'GET':
        r = parse_spec_object(fetch_data())
        print(r)
        return JsonResponse(r, safe=False)
    else:
        return HttpResponse('Not allowed.')


@csrf_exempt
def get_data_by_key(request, pk):
    if request.method == 'GET':
        r = parse_spec_object_by_key((fetch_data_by_key(pk)))
        return JsonResponse(r, safe=False)


@csrf_exempt
def hook(request):
    if request.method == 'POST':
        for obj in serializers.deserialize('json', request.body):
            obj.save()
        return HttpResponse(request.body)


@csrf_exempt
def produce_data(request, pk):
    if request.method == 'GET':
        d = fetch_data_by_key(pk)
        produce(d)
        return HttpResponse("")


def new(request):
    return render(request, 'frontendApp/new.html')


def view(request):
    return render(request, 'frontendApp/index.html')
