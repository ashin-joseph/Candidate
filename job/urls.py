from django.urls import path
from job import views

urlpatterns = [
    path('Index', views.Index, name="Index"),
    path('jobCards', views.jobCards, name="jobCards"),
    path('jobIndividual/<int:user_id>/', views.jobIndividual, name="jobIndividual"),
    path('Trial/', views.Trial, name="Trial"),

    path('', views.candidateandjob, name="candidateandjob"),
    path('candidateProfile/<int:role_id>/', views.candidateProfile, name="candidateProfile"),

]