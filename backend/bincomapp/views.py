from django.shortcuts import render
from .models import announced_pu_results
from django.db.models import Sum
# Create your views here.
def index(request):
    params = {"history":announced_pu_results.objects.all()}

    return render(request, "index.html", params)

def tests(request):
    params = {"history": announced_pu_results.objects.aggregate(Sum("party_score"))["party_score__sum"]}
    return render(request, "tests.html", params)
def results(request):
    params = {"history": announced_pu_results.objects.aggregate(Sum("party_score"))["party_score__sum"]}
    if request.method == 'POST':

        announced_pu_results.result_id=request.POST['result_id']
        announced_pu_results.polling_unit_uniqueid=request.POST['polling_unit_uniqueid']
        announced_pu_results.party_abbreviation=request.POST['party_abbreviation']
        announced_pu_results.party_score=request.POST['party_score']
        announced_pu_results.entered_by_user=request.POST['entered_by_user']
        announced_pu_results.date_entered=request.POST['date_entered']
        announced_pu_results.user_ip_address=request.POST['user_ip_address']
        announced_pu_results.save()
    return render(request, "results.html", params)
