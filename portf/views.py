from django.shortcuts import render
from .models import Project, Certificate, Recommendation


def home(request):
    projects = Project.objects.all()
    certif = Certificate.objects.raw('SELECT * FROM portf_certificate where landscape=FALSE ')
    certif_land = Certificate.objects.raw('SELECT * FROM portf_certificate where landscape=TRUE ')
    recom = Recommendation.objects.all()

    return render(request, 'portf/home.html', {'projects': projects, 'certif': certif, 'certif_land': certif_land, 'recom': recom})