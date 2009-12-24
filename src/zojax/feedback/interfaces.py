from zope import interface
from zope.i18nmessageid.message import MessageFactory
from z3c.schema.email.field import RFC822MailAddress


_ = MessageFactory("zojax.feedback")


class IFeedbackProduct(interface.Interface):
    """ product """

    sendTo = RFC822MailAddress(title=_(u"Send Feedback To"),
                               required=True)
