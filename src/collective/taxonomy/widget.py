import zope.interface
import zope.component
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form.browser.orderedselect import OrderedSelectWidget
from z3c.form.widget import FieldWidget

from plone.app.widgets.dx import RelatedItemsWidget, IRelatedItemsWidget

from interfaces import ITaxonomySelectWidget


class TaxonomySelectWidget(RelatedItemsWidget):
    zope.interface.implements(ITaxonomySelectWidget,
                              IRelatedItemsWidget)


@zope.component.adapter(zope.schema.interfaces.ISequence,
                        interfaces.IFormLayer)
@zope.interface.implementer(interfaces.IFieldWidget)
def TaxonomySelectFieldWidget(field, request):
    """IFieldWidget factory for SelectWidget."""
    return FieldWidget(field, TaxonomySelectWidget(request))
