from django.urls import path
from classroom.views import Categories, CategoryCourses, NewCourse, Enroll, DeleteCourse, EditCourse, MyCourses, CourseDetail


urlpatterns = [
    #course - classroom views
    path('newcourse/', NewCourse, name='newcourse'),
    path('MyCourses/', MyCourses, name='my-courses'),
    path('categories/', Categories, name='categories' ),
    path('categories/<category_slug>',CategoryCourses, name='category-courses'),
    path('<course_id>', CourseDetail, name='course'),
    path('<course_id>/enroll', Enroll, name='enroll'),
    path('<course_id>/edit',EditCourse , name='edit-course'),
    path('<course_id>/delete', DeleteCourse, name='delete-course'),
]