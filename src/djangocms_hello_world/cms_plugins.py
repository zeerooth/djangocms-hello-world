from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import HelloWorldPlugin
from django.utils.translation import ugettext as _


class HelloWorldPluginBase(CMSPluginBase):
    name = _('Hello world plugin')
    model = HelloWorldPlugin
    render_template = "djangocms_hello_world/_hello_world.html"
    allow_children = False

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'custom_text': instance.text,
        })
        return context


plugin_pool.register_plugin(HelloWorldPluginBase)
