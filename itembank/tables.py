import django_tables2 as tables
from .models import MultipleChoiceItem, ShortTextItem

class MultipleChoiceItemTable(tables.Table):
    edit_item = tables.TemplateColumn('<a href="{% url \'itembank:edit_item_MC\' record.id %}">Edit</a>')
    class Meta:
        model = MultipleChoiceItem
        template_name = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table table-bordered table-sm table-hover'}

class ShortTextItemTable(tables.Table):
    edit_item = tables.TemplateColumn('<a href="{% url \'itembank:edit_item_ST\' record.id %}">Edit</a>')
    class Meta:
        model = ShortTextItem
        template_name = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table table-bordered table-sm table-hover' }

class LongTextItemTable(tables.Table):
    edit_item = tables.TemplateColumn('<a href="{% url \'itembank:edit_item_LT\' record.id %}">Edit</a>')
    class Meta:
        model = ShortTextItem
        template_name = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table table-bordered table-sm table-hover' }