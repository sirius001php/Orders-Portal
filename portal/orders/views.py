from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from orders.forms import OrderCreationForm
from orders.models import StatusOrder, Order, Information, OrderHistory, HistoryDescription, SourseAssets
from users.models import MarketPlace
from django.http import HttpResponseRedirect
from django.forms import formset_factory
from django.conf import settings
from django.contrib import messages
from portal.settings import MEDIA_ROOT
import os
@login_required(login_url='users:login_view')
def index(request):
    context = {'title': 'Portal'}
    return render(request, 'orders/index.html', context)


def order_create(request):
    marketplace = MarketPlace.objects.filter(employer_id__user_id=request.user.id)
    if request.method == 'POST':
        form = OrderCreationForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES.getlist('sourse_files'))
        if form.is_valid():
            form.save(request.user, StatusOrder.objects.get(id=1), request.FILES.getlist('sourse_files'))
            return HttpResponseRedirect(reverse('index'))
    else:
        form = OrderCreationForm()
    context = {
        'marketplace' : marketplace,
        'form' : form,
        'title': 'Order create'
    }
    return render(request, 'orders/order-create.html', context)



def order(request, order_id):
    order = Order.objects.get(id=order_id)
    information = Information.objects.get(order_id=order.id)
    history = OrderHistory.objects.filter(order_id=order.id).order_by('-date_creation')
    sourseassets = SourseAssets.objects.filter(order_id=order.id)
    context = {
        'history' : history,
        'order' : order,
        'sourseassets' : sourseassets,
        'title': 'Order',
        'information' : information}
    return render(request, 'orders/order.html', context)

