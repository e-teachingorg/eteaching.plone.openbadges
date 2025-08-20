import hashlib
import secrets
import string

import plone.api
from plone.uuid.interfaces import IUUID


def logged_in_user_name():
    """Get current user id"""
    c = plone.api.user.get_current()
    if c:
        return c.getId()
    return None


def random_string(length):
    """Generate random digits and number"""
    alphabet = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(alphabet) for i in range(length))


def create_identity_hash(email, salt):
    """Create a hash from the recipient's email address"""
    return (
        "sha256$" + hashlib.sha256(email.encode() + salt.encode()).hexdigest()
    )


def create_img_filename(assertion_obj):
    """Create the image filename from obj uuid"""
    assertion_obj_id = IUUID(assertion_obj, None)
    return f"badge-{assertion_obj_id}.svg"
