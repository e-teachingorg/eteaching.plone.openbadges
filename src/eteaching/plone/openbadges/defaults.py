import plone.api


def issuer_name_default():
    # get registry record
    n = "eteaching.plone.openbadges.interfaces.IOpenBadgesSettings.issuer_name"
    return plone.api.portal.get_registry_record(name=n, default=None)


def issuer_url_default():
    # get registry record
    u = "eteaching.plone.openbadges.interfaces.IOpenBadgesSettings.issuer_url"
    return plone.api.portal.get_registry_record(name=u, default=None)


def issuer_description_default():
    # get registry record
    u = "eteaching.plone.openbadges.interfaces.IOpenBadgesSettings.issuer_description"
    return plone.api.portal.get_registry_record(name=u, default=None)


def issuer_email_default():
    # get registry record
    u = "eteaching.plone.openbadges.interfaces.IOpenBadgesSettings.issuer_email"
    return plone.api.portal.get_registry_record(name=u, default=None)
