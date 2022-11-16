from django.shortcuts import render 

def IndexView(request):
    context = {'title':'My Site', 'heading':'Welcome'}
    return render(request, template_name='mysite/index.html', context=context)