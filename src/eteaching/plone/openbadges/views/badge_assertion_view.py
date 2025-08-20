# -*- coding: utf-8 -*-
import datetime
import hashlib
import json

from Acquisition import aq_parent
from Products.Five.browser import BrowserView
from eteaching.plone.openbadges import _
import plone.api
from zope.interface import Interface
from zope.interface import implementer


class IBadgeAssertionView(Interface):
    """Marker Interface for IBadgeAssertionView"""


@implementer(IBadgeAssertionView)
class BadgeAssertionView(BrowserView):

    def assertion_dic(self):
        assertion_json = self.context.get_assertion_json()
        return json.loads(assertion_json)
    
    def get_titles(self, title):
        titles = title.split(": ", 1)
        if len(titles) == 1:
            return {"pre": None, "title": title}
        elif len(titles) == 2:
            return {"pre": titles[0], "title": titles[1]}

    def get_related_content(self):
        relations = []
        r = plone.api.relation.get(
            relationship="learning_resources", source=aq_parent(self.context)
        )
        if r:
            for i in r:
                e = i.to_object
                relations.append({"title": e.title, "url": e.absolute_url()})
        return relations

    def verify_identity(self):
        email = self.request.get("email")
        if email:
            as_dic = self.assertion_dic()
            salt = as_dic["recipient"]["salt"]
            stored_identity = as_dic["recipient"]["identity"]
            h = "sha256$" + hashlib.sha256(
                email.encode() + salt.encode()
            ).hexdigest()
            result = (h == stored_identity)
            return {"result": result, "email": email}
        return {"result": False, "email": ""}

    def linkedin_share(self):
        
        ass = self.assertion_dic()
        
        d = ass["issuedOn"]
        fd = datetime.datetime.fromisoformat(d)
        
        cert_name = ass["badge"]["name"]
        cert_month = fd.date().month
        cert_year = fd.date().year
        cert_url = self.context.absolute_url()
        cert_id = ass["id"].split('/')[-2]
        
        l = (f"https://www.linkedin.com/profile/add"
             f"?startTask=CERTIFICATION_NAME"
             f"&name={cert_name}"
             f"&organizationId=93860123"
             f"&issueYear={cert_year}&issueMonth={cert_month}"
             f"&certUrl={cert_url}&certId={cert_id}")
        
        return l

    def __call__(self):

        return self.index()
