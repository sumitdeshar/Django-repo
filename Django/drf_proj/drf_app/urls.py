from django.urls import path
<<<<<<< HEAD
from drf_app.views import function_based_api_views, function_based_views, class_based_view
=======
from drf_app.views import function_based_api_views, function_based_views
>>>>>>> c2ad93beaa4d06ddc8d85e16a42d16298a40afc7
# from rest_framework.routers import DefaultRouter


urlpatterns = [
    # Function Based View URLS
    # path("student_api", function_based_views.student_api),
    # path("student_api/<int:id>", function_based_views.student_api_detail)

<<<<<<< HEAD
    # # Function Based api View URLS
    # path("student_api", function_based_api_views.StudentAPI),

    #class based views
    path('/', class_based_view.index.as_view())

]

=======
    # Function Based api View URLS
    path("student_api", function_based_api_views.StudentAPI),
]
>>>>>>> c2ad93beaa4d06ddc8d85e16a42d16298a40afc7
