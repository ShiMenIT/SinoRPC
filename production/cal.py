from .models import Operation

#pip install django-filter
#filter product 
#filter time

def dfilter(indicator):
	sdata=Operation.objects.filter(OptProductCode=indicator)
	return sdata

def OEEcal(ind):
	# OEE=Output*OCT/(HO)/3600=OutPut*OCT/(HU+OAD)/3600
	sdata=dfilter(ind)
	Output=sdata.OptGood
	OCT=sdata.OptMachine.OCT
	HU=sdata.OptDuration
	OAD=sdata.OptDownTime
	OEE==OutPut*OCT/(HU+OAD)/3600
	return OEE

#cal
