from Products.Five.browser import BrowserView


class Setup(BrowserView):
    def reimportProfile(self):
        """Reimport eteaching.plone.openbadges profile"""
        portal_setup = self.context.portal_setup
        portal_setup.manage_importAllSteps(
            context_id="profile-eteaching.plone.openbadges:default"
        )
        self.context.plone_utils.addPortalMessage(
            "profile-eteaching.plone.openbadges profile reimported"
        )
        self.request.response.redirect(self.context.absolute_url())
