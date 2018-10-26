from django.apps import apps
from django_tables2 import RequestConfig
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .forms import *
from .tables import *
from .models import MultipleChoiceItem, ShortTextItem, LongTextItem
import pandas as pd

# class created to avoid code repetition in new item views
class NewItem:
    def __init__(self, form_type, request):
        self.form = form_type(request.POST)
        self.post = self.form.save(commit=False)
        self.post.pub_date = timezone.now()
        self.post.save()

# New item views, they call the class above
def new_item_MC(request):
    if request.method == "POST":
        item = NewItem(MultipleChoiceItemForm, request)
        return redirect('itembank:detail_MC', question_id=item.post.pk)
    else:
        form = MultipleChoiceItemForm()
        return render(request, 'itembank/new_item.html', {'form': form})

def new_item_ST(request):
    if request.method == "POST":
        item = NewItem(LongTextItemForm, request)
        return redirect('itembank:detail_ST', question_id=item.post.pk)
    else:
        form = ShortTextItemForm()
        return render(request, 'itembank/new_item.html', {'form': form})

def new_item_LT(request):
    if request.method == "POST":
        item = NewItem(LongTextItemForm, request)
        return redirect('itembank:detail_LT', question_id=item.post.pk)
    else:
        form = LongTextItemForm()
        return render(request, 'itembank/new_item.html', {'form': form})

# edit item views are accessed from index table
def edit_item_MC(request, id):
    item = MultipleChoiceItem.objects.get(pk=id)
    if request.method == "POST":
        form = MultipleChoiceItemForm(request.POST, instance=item)
        form.pub_date = timezone.now()
        form.save()
        return redirect('itembank:detail_MC', question_id=item.pk)
    else:
        form = MultipleChoiceItemForm(instance=item)
        return render(request, 'itembank/new_item.html', {'form': form})

def edit_item_ST(request, id):
    item = ShortTextItem.objects.get(pk=id)
    if request.method == "POST":
        form = ShortTextItemForm(request.POST, instance=item)
        form.pub_date = timezone.now()
        form.save()
        return redirect('itembank:detail_ST', question_id=item.pk)
    else:
        form = ShortTextItemForm(instance=item)
        return render(request, 'itembank/new_item.html', {'form': form})

def edit_item_LT(request, id):
    item = LongTextItem.objects.get(pk=id)
    if request.method == "POST":
        form = ShortTextItemForm(request.POST, instance=item)
        form.pub_date = timezone.now()
        form.save()
        return redirect('itembank:detail_LT', question_id=item.pk)
    else:
        form = LongTextItemForm(instance=item)
        return render(request, 'itembank/new_item.html', {'form': form})

# this needs work
def index(request):
    # takes all models from itembank
    app_models = apps.all_models['itembank']
    item_models = {}
    non_item_models = {}
    count_output = {}
    levels_and_skills = []
    # key is model name lowercase, value is the model
    for key, value in app_models.items():
        # seperates item models from level and skill models
        if "item" in key:
            item_models[key] = value
        else:
            non_item_models[key] = value

    for name, type in non_item_models.items():
        if 'cefr' in name:
            for b in type.objects.all():
                levels_and_skills.append(b)

    for key, model in item_models.items():
        #temp_list = []
        temp_dict = {}
        for x in levels_and_skills:
            temp_dict[str(x)] = model.objects.filter(level__cefr_level=str(x)).count()
        #temp_list.append(temp_dict)
        count_output[key] = temp_dict

    df2 = pd.DataFrame(count_output)

    context = {
        'df2': df2,
        'count_output': count_output,
    }
    return render(request, 'itembank/index.html', (context))

# class created to reduce code repetition in display_items views
class DefineItem:
    def __init__(self, item_type, item_table, item_code):
        self.item_type = item_type
        self.item_table = item_table
        self.get_table = item_table(item_type.objects.order_by('id'))
        self.context = {
            'table': self.get_table,
            'list_count': item_type.objects.count(),
            'header': str(item_type._meta.verbose_name_plural),
            'specific_url': ('itembank:new_item_'+item_code)
        }

    def produce_table(self, request, number_items):
        self.a_table = RequestConfig(request, paginate={'per_page': number_items}).configure(self.get_table)

# displays all items of a given item type
# item type is passed in the url
def display_items_MC(request):
    item = DefineItem(MultipleChoiceItem, MultipleChoiceItemTable, 'MC')
    item.produce_table(request, 10)
    return render(request, 'itembank/disply_items.html', (item.context))

def display_items_ST(request):
    item = DefineItem(ShortTextItem, ShortTextItemTable, 'ST')
    item.produce_table(request, 5)
    return render(request, 'itembank/disply_items.html', (item.context))

def display_items_LT(request):
    item = DefineItem(LongTextItem, LongTextItemTable, 'ST')
    item.produce_table(request, 5)
    return render(request, 'itembank/disply_items.html', (item.context))

# display specifics of an item when it has been clicked on
def detail_MC(request, question_id):
    question_object = get_object_or_404(MultipleChoiceItem, pk=question_id)
    header = str(MultipleChoiceItem._meta.verbose_name)
    context = {
        'question_object': question_object,
        'header': header,
    }
    return render(request, 'itembank/detail.html', (context))

def detail_ST(request, question_id):
    question_object = get_object_or_404(ShortTextItem, pk=question_id)
    header = str(ShortTextItem._meta.verbose_name)
    context = {
        'question_object': question_object,
        'header': header,
    }
    return render(request, 'itembank/detail.html', (context))

def detail_LT(request, question_id):
    question_object = get_object_or_404(LongTextItem, pk=question_id)
    header = str(LongTextItem._meta.verbose_name)
    context = {
        'question_object': question_object,
        'header': header,
    }
    return render(request, 'itembank/detail.html', (context))

