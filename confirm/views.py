from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Wedding, Reservation
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from .forms import ConfirmForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView

class FeedBackViewUpdate(UpdateView):
    model = Reservation
    form_class = ConfirmForm
    template_name = 'confirm/rsvp.html'
    success_url = '/done'

class FeedBackView(CreateView):
    model = Reservation
    form_class = ConfirmForm
    template_name = 'confirm/rsvp.html'
    success_url = '/done'

    # def form_valid(self, form):
    #     form.save()
    #     return super(FeedBackView, self).form_valid(form)
    #
    # def post(self, request):
    #     form = ConfirmForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/done')
    #     return render(request, 'confirm/rsvp.html', context={'form': form})

# class FeedBackView(View):
#     def get(self, request):
#         form = ConfirmForm()
#         return render(request, 'confirm/rsvp.html', context={'form':form})
#
#     def post(self, request):
#         form = ConfirmForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'confirm/rsvp.html', context={'form': form})

class UpdateView(View):
    def get(self, request, id_feedback):
        feed = Reservation.objects.get(id=id_feedback)
        form = ConfirmForm(instance=feed)
        return render(request, 'confirm/rsvp.html', context={'form':form})

    def post(self, request, id_feedback):
        feed = Reservation.objects.get(id=id_feedback)
        form = ConfirmForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
        return render(request, 'confirm/rsvp.html', context={'form': form})

class DoneView(TemplateView):
    template_name = 'confirm/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_id = Reservation.objects.all().last().id
        feedback = Reservation.objects.get(id=last_id)
        context['feedback'] = feedback
        return context

# class GuestFeedBack(TemplateView):
#     template_name = 'confirm/list_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         feedbacks = Reservation.oblects.all()
#         context['feedbacks'] = feedbacks
#         return context

class GuestFeedBack(ListView):
    template_name = 'confirm/list_feedback.html'
    model = Reservation

class FaqPage(TemplateView):
    template_name = 'confirm/faq.html'

def start_page(request):
    return render(request, 'confirm/index.html')

def show_all_guests(request):
    guests = Wedding.objects.all()
    agg = guests.aggregate(Count('id'))
    data = {
        'guests':guests,
        'agg':agg
    }
    return render(request, 'confirm/guests.html', data)

def show_one_guest(request, slug_guest:str):
    guest = get_object_or_404(Wedding, slug=slug_guest)
    data = {
        'guest': guest,
      }
    return render(request, 'confirm/one_guest.html', data)
