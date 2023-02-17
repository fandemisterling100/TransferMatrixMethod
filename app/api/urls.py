from django.urls import include, path
from app.api import views

# Name of this app (folder api) inside of the whole project (folder app)
app_name = "api"

urlpatterns = [
    # URL to receive post data from browser with all the information from the materials
    # and initial parameters. Once the request is received, the view CalculateDataView is
    # going to process it.
    path("transfer-method/", views.CalculateDataView.as_view(), name="calculate"),
    path("download-data/", views.DownloadDataView.as_view(), name="download"),
    path("calculate-chi/", views.CompareExperimentalDataView.as_view(), name="compare_experimental_data"),
]
