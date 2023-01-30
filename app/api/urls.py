from django.urls import include, path
from app.api import views

app_name = "api"

urlpatterns = [
    path("", views.UserViewSet.as_view(), name="example"),
    path("transfer-method/", views.CalculateDataView.as_view(), name="calculate"),
]
