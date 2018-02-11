from django.shortcuts import render,render_to_response
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .import_data import import_data
from .models import *
from django.views.decorators.csrf import csrf_exempt
from registration.forms import RegistrationForm
def index(request):
    if request.method == 'POST':  
        form =OperationForm(request.POST) 
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:  
        form =OperationForm()  
    return render_to_response('production/index.html',locals()) 
# upload file function
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        import_data(filename)
        return render(request, 'production/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'production/upload.html')

@csrf_exempt
def cal(request):
    if request.method=='POST':
        form = OperationForm(request.POST)
        if form.is_valid():
            Line = form.cleaned_data['LineCode']
            Machine = form.cleaned_data['MachineCode']
            StartTime = form.cleaned_data['StartTime']
            EndTime = form.cleaned_data['EndTime']
            result=OEEcal(Line,Machine,StartTime,EndTime)
        else:
            form =OperationForm()
            result=''
    return render(request, 'production/index.html',locals())

def OEEcal(Line,Machine,StartTime,EndTime):
    Lines=Operation.objects.filter(LineCode__LineCode=Line,MachineCode__MachineCode=Machine,StartTime__gte=StartTime,EndTime__lte=EndTime)
    result=[]
    Output=0
    HU=0
    OAD=0
    OCT=int(Lines[1].ProductCode.ProductCT)
    for i in Lines:
        Output+=int(i.Good)
        HU+=int(i.Duration)
        OAD+=int(i.DownTime)
    OEE=Output*OCT/(HU+OAD)/3600
    return OEE
#############################################################
#send data to JS
def getLineCode(request):
    Lines = Line.objects.order_by('LineCode')
    res = []
    for i in Lines:
        res.append( [i.id, i.LineCode] )
    return JsonResponse({'LineCodes':res},safe=False)

def getMachineCode(request):
    Line = request.GET.get('LineCode')
    Machines= Machine.objects.filter(LineCode__LineCode__contains=Line).order_by('MachineCode')
    res = []
    for i in Machines:
        res.append([i.id, i.MachineCode])
    return JsonResponse({'MachineCodes':res},safe=False)

def getDateTime(request):
    Machine=request.GET.get('MachineCode')
    DateTimes= Operation.objects.filter(MachineCode__MachineCode__contains=Machine).order_by('-StartTime','-EndTime')
    res1=[]
    res2=[]
    for i in DateTimes:
        res1.append([i.id, i.StartTime])
        res2.append([i.id, i.EndTime])
    return JsonResponse({'StartTimes': res1,'EndTimes': res2},safe=False)

