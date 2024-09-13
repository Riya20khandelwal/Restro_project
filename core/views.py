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
        name = request.POST.get("user_name")
        p_number = request.POST.get("phone_number")
        email = request.POST.get("user_email")
        t_person = request.POST.get("total_person")
        b_date = request.POST.get("booking_date")
        
        if name != '' and len(p_number) == 10 and email!= "" and t_person != 0 and b_date != "":
            data = BookTable(Name=name, phone_number=p_number,
                             Email=email, Total_person=t_person, Booking_date=b_date)
            data.save()
            # return render(request, 'book_table.html')
    return render(request, 'book_table.html')


def FeedbackView(request):
    if request.method == "POST":
        u_name = request.POST.get("u_name")
        description = request.POST.get("describe")
        rating = request.POST.get("rating")
        u_image = request.FILES.get('u_image')  # Correctly get the uploaded file

        # Convert rating to integer and check for valid inputs
        try:
            rating = int(rating)
        except ValueError:
            rating = 0  # Default to 0 if conversion fails

        # Check if image is uploaded and all required fields are valid
        if u_image and u_name and description and rating > 0:
            f_data = Feedback(User_name=u_name, Description=description, Rating=rating, Image=u_image)  # Use the correct field name
            f_data.save()
            return render(request, 'feedback.html', {'success': True})

        # Check if all fields except image are valid
        elif u_name and description and rating > 0:
            f_data = Feedback(User_name=u_name, Description=description, Rating=rating)  # Use the correct field name
            f_data.save()
            return render(request, 'feedback.html', {'success': True})

    # If it's not a POST request or validation fails, return the form
    return render(request, 'feedback.html')

