from django.shortcuts import HttpResponse, render, redirect
import pymysql
from django.http import JsonResponse
#: python manage.py runserver
#: python manage.py runserver 192.168.43.30:8000
#: python manage.py runserver 10.35.245.91:8000
#: python manage.py runserver 192.168.31.211:8000


def first_experiment(request):

    if request.method == "GET":
        return render(request, 'first_experiment.html', {'name': name, 'age': age, 'sex': sex})
    else:
        print(request.POST)
        number = request.POST.get('number')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='314159', db='steering experiment', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into product_id value(%s)", [number, ])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/first_experiment/')


def second_experiment(request):

    if request.method == "GET":
        return render(request, 'second_experiment.html')
    else:
        print(request.POST)
        number = request.POST.get('number')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='314159', db='table', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into product_id value(%s)", [number, ])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/second_experiment/')

def third_experiment(request):

    if request.method == "GET":
        return render(request, 'third_experiment.html')
    else:
        print(request.POST)
        number = request.POST.get('number')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='314159', db='table', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into product_id value(%s)", [number, ])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/third_experiment/')


def fourth_experiment(request):
    return render(request, 'fourth_experiment.html')


def fifth_experiment(request):
    return render(request, 'fifth_experiment.html')


def sixth_experiment(request):
    return render(request, 'sixth_experiment.html')


def check_data(request):

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='314159', db='table', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select * from product_id")
    product_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, 'check_data.html', {'id_list': product_list})


name = ''
age = 0
sex = ''


def admin(request):
    return render(request, 'admin.html')


def add(request):
    global name, age, sex
    name = request.GET['name']
    age = request.GET['age']
    sex = request.GET['sex']
    name = str(name)
    age = int(age)
    sex = str(sex)
    # print('name:', name)
    # print('age:', age)
    # print('sex:', sex)
    return render(request, 'admin.html')