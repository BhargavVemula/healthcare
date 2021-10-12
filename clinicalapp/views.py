from django.shortcuts import redirect, render
from .models import ClinicalData, Patient
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import ClinicalDataForm

# Create your views here.
class PatientListView(ListView):
    model = Patient

class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ['first_name','last_name','age']

class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ['first_name','last_name','age']

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')


def AddData(request,**kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')     
    return render(request,'clinicalapp/clinicaldata_form.html',{'form':form,'patient':patient})
    
def AnalyseData(request,**kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    response_data = []
    for eachentry in data:
        if eachentry.componentname == 'hw':
            HeightandWeight = eachentry.componentvalue.split('/')
            if len(HeightandWeight)>1:
                feetToMetres = float(HeightandWeight[0]) * 0.4536
                BMI = float(HeightandWeight[1])/(feetToMetres*feetToMetres)
                bmiEntry = ClinicalData()
                bmiEntry.componentname = 'BMI'
                bmiEntry.componentvalue = BMI
                response_data.append(bmiEntry)
        response_data.append(eachentry)
    return render(request,'clinicalapp/generate_response.html',{'data':response_data})