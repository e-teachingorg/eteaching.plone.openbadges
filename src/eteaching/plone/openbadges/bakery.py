from datetime import datetime
import json
from lxml.etree import CDATA
import pytz

from Products.CMFCore.interfaces import IFolderish
from eteaching.plone.openbadges.utils import random_string, create_identity_hash
import lxml.etree as ET
import plone.api
from plone.app.event.base import default_timezone
from plone.uuid.interfaces import IUUID


def create_assertion(badge, logged_in_user=None):
    """Creates and returns and badge assertion object with uid in id"""
    if logged_in_user:
        email = logged_in_user.getProperty("email")
        user_id = logged_in_user.getId()
        if IFolderish.providedBy(badge):
            with plone.api.env.adopt_roles(["Manager"]):
                assertion_object = plone.api.content.create(
                    type="BadgeAssertion",
                    title="Badge Assertion",
                    safe_id=True,
                    container=badge,
                    recipient=user_id,
                    email=email,
                )
                uid = IUUID(assertion_object, None)
                if uid:
                    plone.api.content.rename(
                        obj=assertion_object,
                        new_id=f"{assertion_object.portal_type}{uid}",
                        safe_id=True,
                    )
                plone.api.content.transition(
                    obj=assertion_object, transition="publish"
                )
                assertion_object.reindexObject()
                return assertion_object
    return None


def bake(badge, assertion_obj, logged_in_user, assertion_img_filename):
    """Creates a svg-string, which holds the individual assertion data"""

    recipient_email = logged_in_user.getProperty("email")
    # Create identity hash
    salt = random_string(42)
    identity_hash = create_identity_hash(recipient_email, salt)
    # Create Time stamp in ISO8601 with time zone
    tz = pytz.timezone(default_timezone())
    issued_on = datetime.now(tz=tz).isoformat()
    # Create Payload
    assertion_id = f"{assertion_obj.absolute_url()}/assertion.json"
    issuer_id = f"{assertion_obj.absolute_url()}/issuer"
    badge_image = f"{assertion_obj.absolute_url()}/@@images/image"
    badge_id = f"{assertion_obj.absolute_url()}/download/image/{assertion_img_filename}"
    issuer_data = _issuer(badge, issuer_id)
    badge_data = _badge(badge, badge_id, badge_image, issuer_data)
    recipient_data = _recipient(salt, identity_hash)
    assertion_data = _assertion(
        assertion_id, recipient_data, issued_on, badge_data
    )
    json_assertion_data = json.dumps(assertion_data, indent=4)

    # Baking

    # Register Namespace
    ET.register_namespace("openbadges", "https://openbadges.org/schema/")
    # get image data
    tree = ET.ElementTree(ET.fromstring(badge.image.data))
    # Get SVG root
    root = tree.getroot()
    # Add Namespace to svg root
    ns = "{https://openbadges.org/schema/}"
    root.set(ns + "foobar", "foobar")
    del root.attrib[ns + "foobar"]  # remove unneded foobar
    # Set badge as sub element
    body = ET.SubElement(root, "{https://openbadges.org/schema/}assertion")
    body.attrib["verify"] = assertion_id  # set verifier
    body.text = CDATA(json_assertion_data)  # set payload
    # create string from (xml)svg
    xml_str = ET.tostring(root, xml_declaration=True, encoding="UTF-8")

    return xml_str


def _issuer(badge, issuer_id):
    """Generate issuer data"""
    return {
        "id": issuer_id,
        "type": "Issuer",
        "name": badge.issuer_name,
        "url": badge.issuer_url,
        "description": badge.issuer_description,
        "email": badge.issuer_email,
    }


def _badge(badge, badge_id, badge_image, issuer_data):
    """Generate badge data"""
    prefix = getattr(badge, "title_prefix", None)
    title = badge.title
    if prefix:
        title = f"{prefix}: {badge.title}"
    return {
        "@context": "https://w3id.org/openbadges/v2",
        "type": "BadgeClass",
        "id": badge_id,
        "name": title,
        "description": badge.description,
        "image": badge_image,
        "issuer": issuer_data,
        "criteria": {"narrative": badge.criteria},
        "alignment": [],
    }


def _recipient(salt, identity_hash):
    """Generate recipient data"""
    return {
        "type": "email",
        "identity": identity_hash,
        "hashed": True,
        "salt": salt,
    }


def _assertion(url, recipient_data, issued_on, badge_data):
    """Generate assertion data"""
    return {
        "@context": "https://w3id.org/openbadges/v2",
        "id": url,
        "type": "Assertion",
        "recipient": recipient_data,
        "issuedOn": issued_on,
        "badge": badge_data,
        "verification": {"type": "hosted"},
    }
