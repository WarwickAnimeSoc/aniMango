from django.shortcuts import render
from django.conf import settings


def stream(request):
    stream_url = settings.RTMP_STREAM_URL
    return render(request, 'stream/steam.html', context={'stream_source': stream_url})