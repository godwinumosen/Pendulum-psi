from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponseForbidden
# Create your views here.
from module.forms import NewModuleForm
from module.models import Module
from classroom.models import Course

def NewModule(request, course_id):
    user = request.user
    course = get_object_or_404(Course ,id=course_id)
    
    if user != course.user:
        return HttpResponseForbidden()
    
    else:
        
        if request.method == 'POST':
            form = NewModuleForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data.get('title')
                hours=form.cleaned_data.get('hours')
                m, created =Module.objects.get_or_created(title=title, hours=hours, user=user)
                course.module.add(m)
                course.save()
                return redirect('modules',course_id)
        else:
            form = NewModuleForm()
        
    context ={
        'form':form,   
    }
    return render(request, 'module/newmodule.html', context)


def CourseModule(request, course_id):
    user = request.user
    course = get_object_or_404(Course ,id=course_id)

    teacher_mode = False
    if user == course.user:
        teacher_mode = True
        
    context ={
        'teacher_mode':teacher_mode,  
        'course':course 
    }
    return render(request, 'module/modules.html', context)