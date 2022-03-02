from django.shortcuts import HttpResponse, render, redirect
import pymysql
from django.http import JsonResponse
#: python manage.py runserver
#: python manage.py runserver 192.168.43.30:8000
#: python manage.py runserver 10.35.245.91:8000
#: python manage.py runserver 192.168.31.211:8000
#： python manage.py runserver 10.34.24.117:8000


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


len = 0
wid = 0
time = 0


def admin(request):
    return render(request, 'admin.html')


def save_data(request):
    print(request.GET)
    global len, wid, time
    len = request.GET['len']
    wid = request.GET['wid']
    time = request.GET['time']
    print("len:", len)
    print("wid:", wid)
    print("time:", time)
    if time != '0':
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='314159', db='steering_experiment',
                               charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("insert into steering_data (A,W,time) value(%s,%s,%s)", [len, wid, time, ])
        conn.commit()
        cursor.close()
        conn.close()
    return HttpResponse("")

