import mimetypes
import os
from django.http import HttpResponse, FileResponse

from config import settings


def serve_media(request, path):
    media_path = os.path.join(settings.MEDIA_ROOT, path)
    response = FileResponse(open(media_path, 'rb'))
    content_type = mimetypes.guess_type(path)

    return HttpResponse(response, content_type=content_type)
