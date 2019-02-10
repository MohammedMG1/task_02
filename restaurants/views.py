from django.shortcuts import render

# Create your views here.


# Create your views here.
def my_first_view(request):
    context = {
        'msg': "Hello World!",
        
    }
    return render(request, 'test.html', context)