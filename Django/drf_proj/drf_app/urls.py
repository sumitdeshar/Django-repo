from django.urls import path
from drf_app.views import function_based_api_views, function_based_views, class_based_view
# from rest_framework.routers import DefaultRouter


urlpatterns = [
    # Function Based View URLS
    # path("student_api", function_based_views.student_api),
    # path("student_api/<int:id>", function_based_views.student_api_detail)

    # # Function Based api View URLS
    # path("student_api", function_based_api_views.StudentAPI),

    #class based views
    path('/', class_based_view.index.as_view())

]

