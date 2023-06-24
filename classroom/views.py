from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
from classroom.models import Course, Category
from classroom.forms import NewCourseForm


def index (request):
    user = request.user
    course = Course.objects.filter(enrolled=user)
    
    context = {
        'course':course
    }
    return render(request, 'index.html',context)

def Categories (request):
    categories = Category.objects.all()
    
    context = {
        'categories':categories
    }
    return render(request, 'classroom/categories.html',context)

def CategoryCourses(request, category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    courses = Course.objects.filter(category=category)
    
    context = {
        'category':'category',
        'courses':courses
    }
    return render(request, 'classroom/categorycourses.html',context)




def NewCourse(request):
    user = request.user
    if request.method == 'POST':
        form = NewCourseForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            syllabus = form.cleaned_data.get('syllabus')
            Course.objects.create(picture=picture, title=title, description=description, category=category, syllabus=syllabus, user=user)
            return redirect('my-courses')
    else:
        form = NewCourseForm()
    context = {
        'form':form
    }
    return render(request, 'classroom/newcourse.html',context)
        
@login_required
def Enroll (request, course_id):
    user = request.user
    course = get_object_or_404(Course ,id=course_id)
    course.enrolled.add(user)
    return redirect('index')

@login_required   
def DeleteCourse(request, course_id):
    user = request.user
    course = get_object_or_404(Course ,id=course_id)
    
    if user != course.user:
        return HttpResponseForbidden()
    else:
        course.delete()
    return redirect('my-courses')

@login_required
def EditCourse(request, course_id):
    user = request.user
    course = get_object_or_404(Course ,id=course_id)
    
    if user != course.user:
        return HttpResponseForbidden()
    else:
        
        if request.method == 'POST':
            form = NewCourseForm(request.POST, request.FILES, instance=course)
            if form.is_valid():
                course.picture = form.changed_data.get('picture')
                course.title = form.changed_data.get('title')
                course.description = form.changed_data.get('description')
                course.category = form.changed_data.get('category')
                course.syllabus = form.changed_data.get('syllabus')
                course.save()
                return redirect('my-courses')
        else:
            form = NewCourseForm(instance=course)
    context = {
        'form':form,
        'course':course
    }
    
    return render(request, 'classroom/editcourse.html',context)
            
def MyCourses (request):
    user = request.user
    course = Course.objects.filter(user=user)
    context = {
        'course':course
    }
    return render(request, 'classroom/mycourses.html',context)
            
            
            
            