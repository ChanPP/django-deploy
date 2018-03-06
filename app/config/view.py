import mimetypes
import os

from django.conf import settings
from django.http import HttpResponse, FileResponse



def serve_media(request, path):
    media_path = os.path.join(settings.MEDIA_ROOT, path)
    response = FileResponse(open(media_path, 'rb'))
    content_type = mimetypes.guess_type(path)

    return HttpResponse(response, content_type=content_type)
