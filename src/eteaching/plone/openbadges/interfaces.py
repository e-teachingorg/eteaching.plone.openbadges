# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from eteaching.plone.openbadges import _
from plone.supermodel import model
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IEteachingPloneOpenbadgesLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IOpenBadgesSettings(Interface):

    badge_storage_root = schema.TextLine(
        title=_("badge_storage_root"),
        description=_("help_badge_storage_root"),
        required=False,
        default="community/badges",
    )

    title_prefix_def = schema.Tuple(
        title=_("label_title_prefix_def", default="Title prefixes"),
        description=_("help_title_prefix_def",
                      default="The title prefixes are part of the title and can be predefined here. One prefix is always entered per line."),
        value_type=schema.TextLine(),
        required=False,
    )

    issuer_name = schema.TextLine(
        title=_("label_issuer_name", default="Name"),
        required=False,
    )

    issuer_url = schema.URI(
        title=_("label_issuer_url", default="URL"), required=False
    )

    issuer_description = schema.TextLine(
        title=_("label_issuer_description", default="Description"),
        required=False,
    )

    issuer_email = schema.TextLine(
        title=_("label_issuer_email", default="Email"), required=False
    )

    model.fieldset(
        "issuer",
        label=_("label_schema_issuer", default="Issuer"),
        fields=[
            "issuer_name",
            "issuer_url",
            "issuer_description",
            "issuer_email",
        ],
    )
