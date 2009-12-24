from zope import interface, schema, component
from zope.app.component.hooks import getSite
from zope.app import zapi
from z3c.form.button import buttonAndHandler
from z3c.schema.email.field import RFC822MailAddress
from zojax.layoutform.form import PageletForm
from zojax.layoutform.field import Fields
from zojax.statusmessage.interfaces import IStatusMessage
from zojax.feedback.interfaces import _
from zojax.mailtemplate.interfaces import IMailTemplate
from zojax.controlpanel.interfaces import IConfiglet


class IFeedbackFields(interface.Interface):

    name = schema.TextLine(title=_('Your Name'),
                           required=False)

    email = RFC822MailAddress(title=_(u'Your Email'),
                       required=True)

    subject = schema.TextLine(title=_(u"Subject"), required=True)

    text = schema.Text(title=_(u"Message Text"), required=True)


class FeedbackForm(PageletForm):

    label = _(u'Feedback Form')
    fields = Fields(IFeedbackFields)
    ignoreContext = True

    @buttonAndHandler(_('Send'))
    def handleSend(self, action):
        data, errors = self.extractData()
        if errors:
            IStatusMessage(self.request).add(_('Please fix indicated error.'), 'warning')
            return
        else:
            configlet = component.getUtility(IConfiglet, name='product.zojax-feedback')
            sendTo = configlet.sendTo
            if not sendTo:
                IStatusMessage(self.request).add(_('Unable to send your message. Please try again later.'), 'warning')
                return
            siteURL = zapi.absoluteURL(getSite(), self.request)
            mailTemplate = component.queryMultiAdapter((self, self.request), IMailTemplate, name="zojax.feedback.message")
            data['subject'] = u"[Feedback from %s] %s" % (siteURL, data['subject'])
            mailTemplate.send((sendTo,), **data)
            IStatusMessage(self.request).add(_('Thank you. Your message was sent.'))
            self.request.response.redirect(siteURL)
