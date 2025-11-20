# -*- coding: utf-8 -*-
from datetime import datetime
import pytz
import time

from Products.Five.browser import BrowserView
from eteaching.plone.openbadges import _
from eteaching.plone.openbadges import bakery
from eteaching.plone.openbadges.utils import logged_in_user_name,\
    create_img_filename
import plone.api
from plone.app.event.base import default_timezone
from zope.interface import Interface
from zope.interface import implementer


class IOpenBadgeView(Interface):
    """Marker Interface for IOpenBadgeView"""


@implementer(IOpenBadgeView)
class OpenBadgeView(BrowserView):

    def existing_agreement(self):
        logged_in_user = plone.api.user.get_current()
        if logged_in_user.getId():
            uid = logged_in_user.getId()
            path = self.context.getPhysicalPath()
            path = "/".join(path)
            brains = self.context.portal_catalog(
                recipient=uid, path={"query": path, "depth": 1}
            )
            return brains
        return None

    def get_related_content(self):
        relations = []
        r = plone.api.relation.get(
            relationship="learning_resources", source=self.context
        )
        if r:
            for i in r:
                e = i.to_object
                relations.append({"title": e.title, "url": e.absolute_url()})
        return relations

    def valid_period(self):
        tz = pytz.timezone(default_timezone())
        now = datetime.now(tz=tz)
        start = self.context.allocation_period_start
        end = self.context.allocation_period_end
        if start and end:
            if (now > start) and (now < end):
                return True
        return False

    def __call__(self):
        not_loggedin_msg = _("You must be logged in to be assigned a badge!")
        badge_created_msg = _("Badge created")
        not_created_msg = _("Badge could not be created! Have you confirmed "
                            "that you have met the requirements?")
        agree = self.request.get("agreement")
        form_sent = self.request.get("form_sent")
        if agree and self.valid_period() and not self.existing_agreement():
            badge = self.context
            logged_in_user = plone.api.user.get_current()
            if logged_in_user_name():
                assertion_obj = bakery.create_assertion(
                    badge, logged_in_user)
                assertion_img_filename = create_img_filename(
                    assertion_obj)
                assertion_image = bakery.bake(
                    badge, assertion_obj,
                    logged_in_user,
                    assertion_img_filename)
                assertion_obj.set_assertion_image(
                    assertion_image, assertion_img_filename)
                plone.api.portal.show_message(
                    message=badge_created_msg, request=self.request)
            else:
                plone.api.portal.show_message(
                    message=not_loggedin_msg, request=self.request)
        elif form_sent:
            plone.api.portal.show_message(
                message=not_created_msg, request=self.request)
        return self.index()
