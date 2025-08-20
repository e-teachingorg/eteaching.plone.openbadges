# -*- coding: utf-8 -*-

# from eteaching.plone.openbadges import _
import json
from Products.Five.browser import BrowserView
from zope.interface import Interface
from zope.interface import implementer


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
class IIssuerView(Interface):
    """ Marker Interface for IIssuerView"""


@implementer(IIssuerView)
class IssuerView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('issuer_view.pt')

    def assertion_dic(self):
        assertion_json = self.context.get_assertion_json()
        return json.loads(assertion_json)

    def __call__(self):
        # Implement your own actions:
        return self.index()
