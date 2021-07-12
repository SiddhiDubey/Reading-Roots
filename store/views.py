from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import * 
from .filters import OrderFilter



def store(request):

	products = Product.objects.all()


	myFilter = OrderFilter(request.GET, queryset=products)
	products = myFilter.qs

	context = {'products':products, 'myFilter':myFilter}
	return render(request, 'store/store.html', context)



