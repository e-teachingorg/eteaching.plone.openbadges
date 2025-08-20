from plone.app.content.interfaces import INameFromTitle
from plone.uuid.interfaces import IUUID
from zope.interface import implementer


class INameFromUUID(INameFromTitle):
    def title(self):
        """Return a processed title"""


@implementer(INameFromUUID)
class NameFromUUID(object):

    def __init__(self, context):
        self.context = context

    @property
    def title(self):
        uid = IUUID(self.context, "badge")
        return f"{self.context.portal_type}{uid}"

    def setTitle(self, value):
        return
