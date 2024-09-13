from django.db import models


class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)

    def __str__(self):
        return self.Category_name

class Items(models.Model):
    Item_name= models.CharField(max_length=20)
    description = models.TextField(blank=False)
    Price= models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name="Name", on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
    Description = models.TextField(blank=False)

class Feedback(models.Model):
    User_name = models.CharField(max_length=25)
    Description = models.TextField(blank=False)
    Ratting = models.IntegerField()
    Image = models.ImageField(upload_to='feedback/', blank=True, null=True)
    

    def __str__(self):
        return self.User_name


class BookTable(models.Model):
    Name= models.CharField(max_length=20)
    phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()

    def __str__(self):
        return self.Name
