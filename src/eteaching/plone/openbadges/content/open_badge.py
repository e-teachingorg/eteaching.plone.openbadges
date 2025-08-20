from eteaching.plone.openbadges import _
from eteaching.plone.openbadges.defaults import issuer_description_default
from eteaching.plone.openbadges.defaults import issuer_email_default
from eteaching.plone.openbadges.defaults import issuer_name_default
from eteaching.plone.openbadges.defaults import issuer_url_default
from plone import schema
from plone.app.event.base import default_timezone
from plone.app.z3cform.widgets.datetime import DatetimeWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope.interface import implementer


class IOpenBadge(model.Schema):
    """Marker interface and Dexterity Python Schema for OpenBadge"""

    image = NamedBlobImage(
        title=_("label_image"),
        description=_("help_image"),
        required=True,
    )

    criteria = schema.Text(
        title=_("label_criteria", default="Criteria"),
        description=_(
            "help_criteria", default="Criteria for earning the badge."
        ),
        required=False,
        missing_value="",
    )

    title_prefix = schema.Choice(
        title=_("label_title_prefix", default="Title prefix"),
        description=_(
            "help_title_prefix", default="The title prefix is part of the title and is linked to the title in the badge. The prefix can be entered separately for display on the website. The prefixes are predefined in the OpenBadges settings."
        ),
        vocabulary="eteaching.plone.openbadges.BadgeTypeVocabulary",
        required=False,
    )

    learning_resources = RelationChoice(
        title=_("label_learning_resources", default="Learning resources"),
        description=_(
            "help_learning_resources",
            default="Learning resources the badge belongs to.",
        ),
        vocabulary="plone.app.vocabularies.Catalog",
        required=True,
    )

    allocation_period_start = schema.Datetime(
        title=_("label_allocation_period_start"),
        required=False,
    )
    directives.widget(
        "allocation_period_start",
        DatetimeWidget,
        default_timezone=default_timezone,
    )

    allocation_period_end = schema.Datetime(
        title=_("label_allocation_period_end"),
        required=False,
    )
    directives.widget(
        "allocation_period_end",
        DatetimeWidget,
        default_timezone=default_timezone,
    )

    issuer_name = schema.TextLine(
        title=_("label_issuer_name", default="Name"),
        required=True,
        defaultFactory=issuer_name_default,
    )

    issuer_url = schema.URI(
        title=_("label_issuer_url", default="URL"),
        required=True,
        defaultFactory=issuer_url_default,
    )

    issuer_description = schema.TextLine(
        title=_("label_issuer_description", default="Description"),
        required=True,
        defaultFactory=issuer_description_default,
    )

    issuer_email = schema.TextLine(
        title=_("label_issuer_email", default="Email"),
        required=True,
        defaultFactory=issuer_email_default,
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


@implementer(IOpenBadge)
class OpenBadge(Container):
    """Content-type class for IOpenBadge"""
