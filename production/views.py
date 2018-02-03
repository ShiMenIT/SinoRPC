from django.shortcuts import render,render_to_response
from django.conf import settings
# Create your views here.
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .import_data import import_data
def index(request):
    return render(request, 'production/index.html')
# upload file function
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        #uploaded_file_url = fs.url(filename)
        import_data(filename)
        return render(request, 'production/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'production/upload.html')

#read file to database
