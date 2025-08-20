# -*- coding: utf-8 -*-
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

import logging


logger = logging.getLogger(__name__)


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "eteaching.plone.openbadges:uninstall",
        ]

    def getNonInstallableProducts(self):
        """Hide the upgrades package from site-creation and quickinstaller."""
        return ["eteaching.plone.openbadges.upgrades"]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    add_group_openbadge_manager()


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
    del_group_openbadge_manager()


def add_group_openbadge_manager():
    t = "Create group OpenBadges Manager."
    groups = api.group.get_groups()
    if not any(i.id == "openbadges_manager" for i in groups):
        api.group.create(
            groupname="openbadges_manager",
            title="OpenBadges Manager",
            description="Members can manage OpenBadges and configurations",
            roles=[
                "OpenBadges Manager",
            ],
        )
        logger.info(f"{t} [OK]")
    else:
        logger.info(f"Group OpenBadges Manager already exists.")


def del_group_openbadge_manager():
    groups = api.group.get_groups()
    t = "Delete group OpenBadges Manager."
    r = False
    if any(i.id == "openbadges_manager" for i in groups):
        r = api.group.delete(groupname="openbadges_manager")
        if r:
            logger.info(f"{t} [OK]")
        else:
            logger.info(f"{t} [Clould not be deleted]")
    else:
        logger.info(f"{t} [Group not found]")
