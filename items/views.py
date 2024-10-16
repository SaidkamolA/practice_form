from django.shortcuts import render, redirect
import math

from items.forms import ItemCreationForm
from items.models import Item


def index(request):
    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 5))
    offset = int((page - 1) * limit)
    items = Item.objects.all()
    all_p = math.ceil(len(items) / limit)
    items = items[offset:offset + limit]
    return render(request, 'items/index.html',
                  {'items': items,
                   'page': page,
                   'limit': limit,
                   'all_p': all_p,
                   })


def get_item(request, pk):
    item = Item.objects.get(id=pk)
    context = {
        'item': item
    }
    return render(request, 'items/item_detail.html', context)


def dobavlenie(request):
    if request.method == 'POST':
        if 'name' in request.POST and 'description' in request.POST and 'price' in request.POST and 'count' in request.POST and 'category_id':
            name = request.POST['name']
            desc = request.POST['description']
            price = request.POST['price']
            count = request.POST['count']
            category_id = request.POST['category_id']
            Item.objects.create(name=name, description=desc, price=price, count=count, category_id=category_id)
        return render(request, 'items/index.html')
    else:
        return render(request, 'items/dob.html')


def izmen(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['description']
        price = request.POST['price']
        count = request.POST['count']
        category_id = request.POST['category_id']
        item.name = name
        item.description = desc
        item.price = price
        item.count = count
        item.category_id = category_id
        item.save()
        return render(request, 'items/index.html')
    else:
        return render(request, 'items/izm.html')


def udalenie(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        # return render(request, 'items/index.html')
        return redirect('index')
        # return redirect('get_item', 2) 2 это pk
    else:
        return render(request, 'items/udalenie.html')


def create(request):
    form = ItemCreationForm()

    item = Item.objects.first()

    if request.method == 'POST':
        # form = ItemCreationForm(request.POST, instance=item)
        form = ItemCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'items/index.html')

    return render(request, 'items/dob2.html',
                  {'form': form})




















# def st(request):
#     if request.method == 'POST':
#         pass
#     else:
#         page = request.GET.get
#         limit = 10
#         offset = (page - 1) * limit
#         end = offset + limit
#         items = Item.objects.all()[offset:end]
