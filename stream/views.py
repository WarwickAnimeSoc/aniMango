from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import timezone

from .models import ViewCounter, View


def stream(request):
    stream_url = settings.RTMP_STREAM_URL
    return render(request, 'stream/steam.html', context={'stream_source': stream_url})


def view(request, token):
    view_counter = ViewCounter.objects.get(id=1)
    try:
        view_object = View.objects.get(token=token)
    except View.DoesNotExist:
        view_object = None

    if view_object:
        view_object.last_update = timezone.now()
        view_object.save()
    else:
        try:
            new_view = View(counter=view_counter, token=token, last_update=timezone.now())
            new_view.save()
        except IntegrityError:
            return redirect('stream:stream')

    return redirect('stream:stream')


def view_count(request):
    view_counter = ViewCounter.objects.get(id=1)
    view_counter.prune()
    view_counter.save()
    return render(request, 'stream/viewcount.html', context={'views': view_counter.count()})