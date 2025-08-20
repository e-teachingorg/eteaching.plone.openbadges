from plone import api
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


# users = [f"{user.getProperty('fullname')} ({user.getUserName()})" for user in api.user.get_users()]


@implementer(IVocabularyFactory)
class UserVocabulary(object):
    """User vocabulary with IDs for a user choice field"""

    def __call__(self, context):
        terms = []
        for user in api.user.get_users():
            value = user.getUserName()
            title = f"{user.getProperty('fullname')} ({value})"
            terms.append(SimpleTerm(value=value, token=value, title=title))
        return SimpleVocabulary(terms)


UserVocabularyFactory = UserVocabulary()


@implementer(IVocabularyFactory)
class BadgeTypeVocabulary(object):
    """Badge type vocabulary"""

    def __call__(self, context):
        terms = []
        bt = "eteaching.plone.openbadges.interfaces.IOpenBadgesSettings.title_prefix_def"
        bt_vocab = api.portal.get_registry_record(name=bt, default=None)
        if bt_vocab:
            for entry in bt_vocab:
                terms.append(SimpleTerm(value=entry, token=entry, title=entry))
        return SimpleVocabulary(terms)


BadgeTypeVocabularyFactory = BadgeTypeVocabulary()
