from django.urls import path
from job import views

urlpatterns = [
    path('', views.jobIndex, name="jobIndex"),
    path('jobIndividual/<int:user_id>/', views.jobIndividual, name="jobIndividual"),
    path('jobProfiles', views.jobProfiles, name="jobProfiles"),
    path('candidateandjob', views.candidateandjob, name="candidateandjob"),
]