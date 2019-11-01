import django_tables2 as tables
from .models import Test

class TestTable(tables.Table):
    select = tables.TemplateColumn('<button name="{{ record.id }}" id="select_button">select</button>')
    class Meta:
        model = Test
        fields = ("name", "description")
        attrs = {'class': 'table table-bordered table-sm table-hover'}