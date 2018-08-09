from django.apps import apps
from django.shortcuts import get_object_or_404, render, redirect
from .forms import MultipleChoiceItemForm, ShortTextItemForm


# Create your views here.
def new_item(request, item_type):
    if item_type == "MultipleChoiceItem":
        item_form = MultipleChoiceItemForm
    else:
        item_form = ShortTextItemForm
    if request.method == "POST":
        form = item_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('itembank:detail', {'item_form': item_form, 'pk': post.pk})
    else:
        form = item_form()
    context = {
        'form': item_form,
        'item_type': item_type
    }
    return render(request, 'itembank/new_item.html', context)


def index(request):
    # takes all models from itembank
    app_models = apps.all_models['itembank']
    model_counts = {}
    non_items = []
    # key is model name lowercase, value is the model
    for key, value in app_models.items():
        # adds to dictionary with model name and number of model objects created
        if "item" in key:
            model_counts[str(value._meta.verbose_name_plural)] = value.objects.all()
        else:
            non_items.append(value.objects.all())
    context = {
        'app_models': app_models,
        'model_counts': model_counts,
        'non_items': non_items
    }
    return render(request, 'itembank/index.html', (context))


# displays all items of a given item type
# item type is passed in the url
def display_items(request, item_type):
    ItemType = apps.get_model(app_label='itembank', model_name=item_type)
    latest_question_list = ItemType.objects.order_by('id')[:5]
    header = str(ItemType._meta.verbose_name_plural)
    name_pass = str(ItemType._meta.object_name)
    headers = ['ID', 'Question', 'CEFR Level', 'Type', 'Published']
    context = {
        'latest_question_list': latest_question_list,
        'header': header,
        'headers': headers,
        'name_pass': name_pass,
    }
    return render(request, 'itembank/disply_items.html', (context))

# display specifics of an item when it has been clicked on
def detail(request, item_type, question_id):
    ItemType = apps.get_model(app_label='itembank', model_name=item_type)
    question_object = get_object_or_404(ItemType, pk=question_id)
    header = str(ItemType._meta.verbose_name)
    context = {
        'question_object': question_object,
        'header': header,
    }
    return render(request, 'itembank/detail.html', (context))

