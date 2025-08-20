# -*- coding: utf-8 -*-
from xml.dom import minidom

from eteaching.plone.openbadges import _
from plone import schema
from plone.app.z3cform.widgets.select import Select2FieldWidget
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile.field import NamedBlobImage
from plone.namedfile.file import NamedBlobImage as NamedBlobImageFile
from plone.supermodel import model
from zope.interface import implementer


class IBadgeAssertion(model.Schema):
    """Marker interface and Dexterity Python Schema for BadgeAssertion"""

    title = schema.TextLine(
        title=_("label_title", default="Title"), required=True
    )

    image = NamedBlobImage(
        title=_("label_image"),
        description=_("help_image"),
        required=False,
        readonly=True,
    )

    directives.widget(
        "recipient", Select2FieldWidget, pattern_options={"width": "100%"}
    )
    recipient = schema.Choice(
        title=_("label_recipient"),
        vocabulary="eteaching.plone.openbadges.UserVocabulary",
        required=False,
        readonly=True,
    )

    email = schema.Email(
        title=_("label_email"),
        readonly=True,
    )


@implementer(IBadgeAssertion)
class BadgeAssertion(Item):
    """Content-type class for IBadgeAssertion"""

    def set_assertion_image(self, svg_data, filename="openbadge.svg"):
        """Creates the data for the badge in SVG format"""
        self.image = NamedBlobImageFile(
            data=svg_data, filename=filename, contentType="image/svg+xml"
        )

    def get_assertion_json(self):
        payload = None
        data = minidom.parseString(self.image.data)
        parts = data.getElementsByTagName('openbadges:assertion')
        for part in parts:
            for node in part.childNodes:
                if node:
                    payload = node.nodeValue
        return payload
