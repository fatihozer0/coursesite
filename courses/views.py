from django.shortcuts import render

def course_list(request):
    return render(request, 'courses.html')