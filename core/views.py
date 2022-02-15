from django.shortcuts import get_object_or_404, redirect, render
from core.forms import LeaveForm

from core.models import Leave

# Create your views here.

def leave_list_view(request):
    leave_requests = Leave.objects.all()
    context = {
        'leave_requests':leave_requests
    }
    return render(request, 'leave_request_list.html', context)

def new_leave_request(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LeaveForm()
    
    return render(request, 'add_leave_request.html', {'form':form})

def update_leave_request(request, id):
    context ={}

    obj = get_object_or_404(Leave, id = id)
 
    form = LeaveForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return redirect('home')

    context["form"] = form
 
    return render(request, "update_leave_request.html", context)