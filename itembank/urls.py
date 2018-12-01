from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'itembank'
urlpatterns = [
    # ex: /itembank/
    path('', views.index, name='index'),
    path('itembank/', views.index, name='index'),
    # ex: /itembank/MultipleChoiceItem/
    path('itembank/MultipleChoiceItem/', views.display_items_MC, name='display_MC'),
    path('itembank/ShortTextItem/', views.display_items_ST, name='display_ST'),
    path('itembank/LongTextItem/', views.display_items_LT, name='display_LT'),
    # ex: /itembank/MultipleChoiceItem/5
    path('itembank/MultipleChoiceItem/<int:question_id>/', views.detail_MC, name='detail_MC'),
    path('itembank/ShortTextItem/<int:question_id>/', views.detail_ST, name='detail_ST'),
    path('itembank/LongTextItem/<int:question_id>/', views.detail_LT, name='detail_LT'),
    path('itembank/MultipleChoiceItem/<int:id>', views.edit_item_MC, name='edit_item_MC'),
    path('itembank/ShortTextItem/<int:id>', views.edit_item_ST, name='edit_item_ST'),
    path('itembank/ShortTextItem/<int:id>', views.edit_item_LT, name='edit_item_LT'),
    # ex: /;itembank/MultipleChoiceItem/new
    path('itembank/ShortTextItem/new_item', views.new_item_ST, name='new_item_ST'),
    path('itembank/MultipleChoiceItem/new_item', views.new_item_MC, name='new_item_MC'),
    path('itembank/LongTextItem/new_item', views.new_item_LT, name='new_item_LT'),
]
'''
    accounts/ login/ [name='login'] #works
    accounts/ logout/ [name='logout'] #works
    accounts/ password_change/ [name='password_change'] #goes to django admin
    accounts/ password_change/done/ [name='password_change_done'] # goes to django admin
    accounts/ password_reset/ [name='password_reset'] #works
    accounts/ password_reset/done/ [name='password_reset_done'] #works but link doesn't from pass
    accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm'] 
    accounts/ reset/done/ [name='password_reset_complete'] #works after adding itembank: to url

#Add Django site authentication urls (for login, logout, password management)
#app_name = ''
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
'''