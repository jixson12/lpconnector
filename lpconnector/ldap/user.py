import re
from ..lastpass.user import LastPassUser


class LDAPUser(object):

    OBJECT_CLASS = "inetOrgPerson"
    ATTRIBUTES = ["uid", "mail", "cn", "memberOf"]

    def __init__(self, **kwargs):
        self.uid = kwargs.get('uid')[0]
        self.email = kwargs.get('mail')[0]
        self.name = kwargs.get('cn')[0]
        group_list = []
        for dn in kwargs.get('memberOf'):
            cn = re.match("cn=(.*),ou", dn)
            if cn:
                group_list.append(cn.group(1))
        self.groups = group_list

    def get_lastpass_user(self):
        return LastPassUser(
            username=self.email,
            fullname=self.name,
            groups=self.groups,
            attribs={'uid': self.uid}
        )
