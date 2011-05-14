# django imports
from django.utils.translation import ugettext_lazy as _

# lfc imports
from lfc.utils.registration import register_content_type
from lfc.utils.registration import unregister_content_type
from lfc.utils.registration import register_sub_type
from lfc.utils.registration import register_template
from lfc.utils.registration import unregister_template

# portlets imports
from portlets.utils import register_portlet
from portlets.utils import unregister_portlet

# lfc_contact_form import
from lfc_contact_form.models import ContactForm

name = "Contact Form"
description = _(u"Contact form for LFC")

def install():
    """Installs the lfc_contact_form application.
    """
    # Register Templates
    register_template(name="Contact Form", path="lfc_contact_form/contact_form.html")

    # Register objects
    register_content_type(ContactForm, name = "Contact", templates=["Contact Form"], default_template="Contact Form", global_addable=True, workflow="Portal")
    
def uninstall():
    """Uninstalls the lfc_contact_form application.
    """
    # unregister your stuff here
    unregister_content_type("ContactForm")

    # Unregister template
    unregister_template("Contact Form")
