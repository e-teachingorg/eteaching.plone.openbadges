# -*- coding: utf-8 -*-
from eteaching.plone.openbadges.content.badge_assertion import (
    IBadgeAssertion,  # NOQA E501
)
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


class BadgeAssertionIntegrationTest(unittest.TestCase):

    layer = ETEACHING_PLONE_OPENBADGES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            "OpenBadge",
            self.portal,
            "parent_container",
            title="Parent container",
        )
        self.parent = self.portal[parent_id]

    def test_ct_badge_assertion_schema(self):
        fti = queryUtility(IDexterityFTI, name="BadgeAssertion")
        schema = fti.lookupSchema()
        self.assertEqual(IBadgeAssertion, schema)

    def test_ct_badge_assertion_fti(self):
        fti = queryUtility(IDexterityFTI, name="BadgeAssertion")
        self.assertTrue(fti)

    def test_ct_badge_assertion_factory(self):
        fti = queryUtility(IDexterityFTI, name="BadgeAssertion")
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IBadgeAssertion.providedBy(obj),
            "IBadgeAssertion not provided by {0}!".format(
                obj,
            ),
        )

    def test_ct_badge_assertion_adding(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        obj = api.content.create(
            container=self.parent,
            type="BadgeAssertion",
            id="badge_assertion",
        )

        self.assertTrue(
            IBadgeAssertion.providedBy(obj),
            "IBadgeAssertion not provided by {0}!".format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn("badge_assertion", parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn("badge_assertion", parent.objectIds())

    def test_ct_badge_assertion_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="BadgeAssertion")
        self.assertFalse(
            fti.global_allow, "{0} is globally addable!".format(fti.id)
        )
