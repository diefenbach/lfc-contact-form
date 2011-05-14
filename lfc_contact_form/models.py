# django imports
from django import forms
from django.db import models

# django imports
from django import forms
from django import template
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_syncdb
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

# lfc imports
import lfc.utils
from lfc.models import BaseContent

# lfc_contact_form imports
from lfc_contact_form.forms import ContactForm as DjangoContactForm


class ContactForm(BaseContent):
    """Contact form for LFC.
    """
    text = models.TextField(blank=True)
    thank_you_message = models.TextField(blank=True)

    def edit_form(self, **kwargs):
        """Returns the add/edit form of the Blog
        """
        return ContactFormForm(**kwargs)

    def render(self, request):
        """Renders the content of the contact form.
        """
        render_context = self.get_render_context(request)

        if request.method == "POST":
            form = DjangoContactForm(data=request.POST)
            if form.is_valid():
                sent = True
                # send mail
            else:
                sent = False
        else:
            form = DjangoContactForm()
            sent = False

        render_context["sent"] = sent
        render_context["form"] = form

        return self.render_to_string(render_context)

class ContactFormForm(forms.ModelForm):
    """The add/edit form of the ContactForm content object.
    """
    class Meta:
        model = ContactForm
        fields = ("title", "display_title", "slug", "description", "text", "thank_you_message")
