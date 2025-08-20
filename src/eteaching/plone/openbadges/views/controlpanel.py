from eteaching.plone.openbadges import _
from eteaching.plone.openbadges.interfaces import IOpenBadgesSettings
from plone.app.registry.browser import controlpanel
from Products.Five.browser import BrowserView


class OpenBadgeSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IOpenBadgesSettings
    label = _("OpenBadges settings")
    description = ""

    def updateFields(self):
        super(OpenBadgeSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(OpenBadgeSettingsEditForm, self).updateWidgets()


class OpenBadgeSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = OpenBadgeSettingsEditForm


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
