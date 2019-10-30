from django.shortcuts import render, redirect, render_to_response

from django.http import HttpResponse

from .models import Student

def search_form(request):
    return render_to_response('index.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        students = Student.objects.filter(last_name__icontains=q)
        return render_to_response('search_results.html',
            {'students': students, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

def index(request):
    students = Student.objects.all()
    context = {
        'students': students
    }

    return render(request, 'index.html', context)

def add_student(request):
    if (request.method == "POST"):
        name = request.POST['name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        group = request.POST['group']
        mark = request.POST['mark']
        city = request.POST['city']
        year = request.POST['year']
        gender = request.POST['gender']
        if gender == "Муж":
            gender = True
        else:
            gender = False


        student = Student(name=name, last_name=last_name, email=email, group=
                            group, mark=mark, city=city, year=year, gender=gender)
        student.save()

        return redirect('/')
    else:
        return render(request, 'add_student.html', {})

