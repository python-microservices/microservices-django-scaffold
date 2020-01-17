import uuid

from django.db import models


class AppModel(models.Model):
    """Set the shared fields of all Models.
    Attrs:
        idpublic: is the field used to get instances and when the id is exposed in urls,
        POST, GET methods.
    """
    idpublic = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name=u'Número de referencia')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
