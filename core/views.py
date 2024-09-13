from django.shortcuts import render, redirect
from core.models import *

def HomeView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    data = AboutUs.objects.all()
    return render(request, 'home.html', {
        'items':items,
        'list': list,
        'review': review,
        'data':data,
    })

def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html', locals())

def MenuView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {
        'items':items,
        'list': list,
    })

def BookTableView(request):
    if request.method == "POST":
        name = request.method.get("user_name")
        p_number = request.method.get("phone_number")
        email = request.method.get("user_email")
        t_person = request.method.get("total_person")
        b_date = request.method.get("booking dte")
        
        if name != '' and len(p_number) == 10 and email!= "" and t_person != 0 and b_date != "":
            data = BookTable(Name=name, phone_number=p_number,
                             Email=email, Total_person=t_person, Booking_date=b_date)
            data.save()
    return render(request, 'book_table.html')

def FeedbackView(request):
    return render(request, 'feedback.html')
