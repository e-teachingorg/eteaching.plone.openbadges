# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
from eteaching.plone.openbadges import _
from zope.interface import Interface
from zope.interface import implementer


class IAssertionView(Interface):
    """ Marker Interface for IAssertionView"""


@implementer(IAssertionView)
class AssertionView(BrowserView):

    def __call__(self):
        assertion = self.context.get_assertion_json()
        if assertion:
            self.context.REQUEST.RESPONSE.setHeader(
                "Content-type", "application/json"
            )
            return assertion
        return _("No assertion available")
