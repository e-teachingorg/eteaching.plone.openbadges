# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from eteaching.plone.openbadges.testing import (  # noqa: E501
    ETEACHING_PLONE_OPENBADGES_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that eteaching.plone.openbadges is properly installed."""

    layer = ETEACHING_PLONE_OPENBADGES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if eteaching.plone.openbadges is installed."""
        self.assertTrue(
            self.installer.is_product_installed("eteaching.plone.openbadges")
        )

    def test_browserlayer(self):
        """Test that IEteachingPloneOpenbadgesLayer is registered."""
        from eteaching.plone.openbadges.interfaces import IEteachingPloneOpenbadgesLayer
        from plone.browserlayer import utils

        self.assertIn(IEteachingPloneOpenbadgesLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ETEACHING_PLONE_OPENBADGES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("eteaching.plone.openbadges")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if eteaching.plone.openbadges is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed("eteaching.plone.openbadges")
        )

    def test_browserlayer_removed(self):
        """Test that IEteachingPloneOpenbadgesLayer is removed."""
        from eteaching.plone.openbadges.interfaces import IEteachingPloneOpenbadgesLayer
        from plone.browserlayer import utils

        self.assertNotIn(
            IEteachingPloneOpenbadgesLayer, utils.registered_layers()
        )
