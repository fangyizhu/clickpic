from django.http import HttpResponse
import json


def index(request):
    return HttpResponse("bapo")
    #return HttpResponse(json.dumps(result.as_json()), content_type="application/json")