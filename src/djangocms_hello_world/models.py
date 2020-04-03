from cms.models.pluginmodel import CMSPlugin
from django.db import models


class HelloWorldPlugin(CMSPlugin): # pylint: disable=model-no-explicit-unicode
    text: models.TextField = models.TextField("Your custom text", null=True, blank=True)

    class Meta:
        verbose_name = "Hello world plugin"
        verbose_name_plural = "Hello world plugins"
