from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html lang='en'><body>It is now {now}.</body></html>"
    return HttpResponse(html)
