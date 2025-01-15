from django.urls import path
from restapp.views import home, UploadJob, UploadCv

urlpatterns = [
    path('', home, name='home'),
    path('upload-job/', UploadJob.as_view(), name='upload_job'),
    path('upload-CV/', UploadCv.as_view(), name='upload_CV')
]