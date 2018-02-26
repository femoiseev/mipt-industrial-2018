from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import td_item
from .forms import user_add

# Get items from database
def index(request):
    form = user_add()
    items = td_item.objects.order_by('-date_added')

    return render(request, 'index/index.html', {'form': form, 'items': items})

# Add items to database
@require_POST
def add(request):

    # Post Request
    if request.method == 'POST':
        form = user_add(request.POST)

        if form.is_valid():
            new_item = td_item(item=request.POST['item'])
            new_item.save()
            return redirect('index')
    
    # Get Request
    else:
        return redirect('index')

# Mark items as completed from database
def complete(request, td_id):
    td_bool = td_item.objects.get(pk=td_id)
    td_bool.complete = True
    td_bool.save()
    return redirect('index')

# Delete items from database
def delete(request, td_id):

    td_item.objects.get(pk=td_id).delete()
    return redirect('index')

# Delete items marked as complete from database
def deletecomplete(request):
    td_item.objects.exclude(complete=False).delete()
    return redirect('index')

# Delete all items from database
def deleteall(request):
    td_item.objects.all().delete()
    # migrations.RunSQL(ALTER TABLE td_item AUTO_INCREMENT=1;)
    return redirect('index')

