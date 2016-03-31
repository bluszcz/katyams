from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

class Foundation6Rowlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "foundation6/row_plugin.html"
    cache = False
    allow_children = True
    module = "Foundation 6 by Katia Deer mimimi mi"
    name = "Row"

plugin_pool.register_plugin(Foundation6Rowlugin)