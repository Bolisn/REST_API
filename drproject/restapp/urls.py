from django.urls import path
from restapp.views import home, UploadJob

urlpatterns = [
    path('', home, name='home'),
    path('upload-job/', UploadJob.as_view(), name='upload_job'),
]