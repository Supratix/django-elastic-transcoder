import django.dispatch

# (providing_args=["job", "message"]

transcode_onprogress = django.dispatch.Signal()
transcode_onerror = django.dispatch.Signal()
transcode_oncomplete = django.dispatch.Signal()
transcode_onwarning = django.dispatch.Signal()
