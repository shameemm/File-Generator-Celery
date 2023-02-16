from django.shortcuts import render
from django.http import HttpResponse
from .tasks import run_generate_file_task


def test(request):
    if request.method == 'POST':
        file_name = str(request.POST.get('filename'))
        count = int(request.POST.get('count'))
        run_generate_file_task(file_name,count)
    else:
        return render(request, 'generator-form.html')
    return HttpResponse("File is generated check data folder")