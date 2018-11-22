


class Contact:
    def __init__(self, firstname = None, lastname = None, address = None, home_phone = None, mobile_phone = None,
                 work_phone = None, email = None, address2 = None, phone2 = None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.email = email
        self.address2 = address2
        self.phone2 = phone2

    # def __repr__(self):
    #     return "%s:%s" % (self.id, self.name)
    #
    # def __eq__(self, other):
    #     return self.id == other.id and self.name == other.name
