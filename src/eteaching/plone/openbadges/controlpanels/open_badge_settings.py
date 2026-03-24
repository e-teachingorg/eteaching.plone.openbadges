from eteaching.plone.openbadges import _
from eteaching.plone.openbadges.interfaces import IOpenBadgesSettings
from plone.app.registry.browser import controlpanel


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
