# -*- coding: utf-8 -*-
from eteaching.plone.openbadges.content.open_badge import IOpenBadge  # NOQA E501
from eteaching.plone.openbadges.testing import (  # noqa
    ETEACHING_PLONE_OPENBADGES_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


class OpenBadgeIntegrationTest(unittest.TestCase):

    layer = ETEACHING_PLONE_OPENBADGES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.parent = self.portal

    def test_ct_open_badge_schema(self):
        fti = queryUtility(IDexterityFTI, name="OpenBadge")
        schema = fti.lookupSchema()
        self.assertEqual(IOpenBadge, schema)

    def test_ct_open_badge_fti(self):
        fti = queryUtility(IDexterityFTI, name="OpenBadge")
        self.assertTrue(fti)

    def test_ct_open_badge_factory(self):
        fti = queryUtility(IDexterityFTI, name="OpenBadge")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IOpenBadge.providedBy(obj),
            "IOpenBadge not provided by {0}!".format(
                obj,
            ),
        )

    def test_ct_open_badge_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.portal,
            type="OpenBadge",
            id="open_badge",
        )

        self.assertTrue(
            IOpenBadge.providedBy(obj),
            "IOpenBadge not provided by {0}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("open_badge", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("open_badge", parent.objectIds())

    def test_ct_open_badge_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="OpenBadge")
        self.assertTrue(
            fti.global_allow, "{0} is not globally addable!".format(fti.id)
        )

    def test_ct_open_badge_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="OpenBadge")
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            "open_badge_id",
            title="OpenBadge container",
        )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type="Document",
            title="My Content",
        )
        self.assertTrue(
            obj, "Cannot add {0} to {1} container!".format(obj.id, fti.id)
        )
