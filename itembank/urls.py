from django.urls import path

from . import views

app_name = 'itembank'
urlpatterns = [
    # ex: /itembank/
    path('', views.index, name='index'),
    path('itembank/', views.index, name='index'),
    # ex: /itembank/MultipleChoiceItem/
    path('itembank/<slug:item_type>/', views.display_items, name='display'),
    # ex: /itembank/MultipleChoiceItem/5
    path('itembank/<slug:item_type>/<int:question_id>/', views.detail, name='detail'),
    # ex: /;itembank/MultipleChoiceItem/new
    path('itembank/<slug:item_type>/new_item', views.new_item, name='new_item'),
]
