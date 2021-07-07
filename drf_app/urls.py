from django.urls import path, include
from .views import (
    EmployeeViewSet,
    EmployeeCreate,
    EmployeeList,
    EmployeeRetrive,
    EmployeeUpdate,
    EmployeeDelete,
    EmployeeCreateList,
    EmployeeRetriveUpdateDelete,
    EmployeeView,
    EmployeeDetail,
    UserViewSet,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("employees", EmployeeViewSet)
router.register("user", UserViewSet)

urlpatterns = [
    path("create/", EmployeeCreate.as_view(), name="create"),
    path("", EmployeeList.as_view(), name="list"),
    path("retrive/<int:pk>/", EmployeeRetrive.as_view(), name="retrive"),
    path("update/<int:pk>/", EmployeeUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", EmployeeDelete.as_view(), name="delete"),
    path("create_list/", EmployeeCreateList.as_view(), name="create_list"),
    path(
        "ret_upd_del/<int:pk>/",
        EmployeeRetriveUpdateDelete.as_view(),
        name="ret_upd_del",
    ),
    path("emp/", EmployeeView.as_view(), name="test"),
    path("emp/<int:pk>/", EmployeeDetail.as_view(), name="employee_detail"),
] + router.urls
