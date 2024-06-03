from django.shortcuts import render

def balance(request):
    context = {'title': 'Balance'}
    return render(request, 'balance/balance.html', context)

