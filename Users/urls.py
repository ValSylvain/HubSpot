from django.conf.urls import url, include

from Users.views import dashboard, registration

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^registration/", registration, name="registration")

]