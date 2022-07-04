from django.urls import path
from .views import start_page, show_one_guest, show_all_guests, FeedBackView, UpdateView, DoneView, FaqPage, GuestFeedBack, FeedBackViewUpdate

urlpatterns = [
    path('', start_page, name='main_page'),

    path('faq', FaqPage.as_view()),
    path('rsvp/', FeedBackView.as_view()),
    path('guests', show_all_guests),
    path('guests/<str:slug_guest>', show_one_guest, name='guest_detail'),
    path('rsvp/<int:id_feedback>', UpdateView.as_view()),
    path('list', GuestFeedBack.as_view()),
    path('done', DoneView.as_view()),
    path('update/<int:pk>',FeedBackViewUpdate.as_view())
]