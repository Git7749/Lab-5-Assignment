from django.http import HttpResponse
import json
def index(request):

    data = {"message" : "Hello World!"}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')
