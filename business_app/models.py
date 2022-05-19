from email.policy import default
from django.contrib.auth.models import User
from django.db import models

# contact
class contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.pk) +"."+" "+ self.name


class Message_Manu(models.Model):
    Message = models.CharField(max_length=50)
    def __str__(self):
        return self.Message


# all frontend orders
class Frontend_Order(models.Model):
    USer = models.ForeignKey(User,default=None,on_delete=models.CASCADE,related_name='user_frontend_order')
    Service_Type = models.CharField(max_length=250, null=True)
    Price = models.CharField(max_length=250, null=True)
    Number_of_Section = models.CharField(max_length=250, null=True)
    Per_section_Price = models.CharField(max_length=250, null=True)
    Website_Functionality = models.CharField(max_length=50, null=True)
    Email = models.EmailField(max_length=50, null=True)
    files = models.FileField(upload_to="0_frontend_files/", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    order_message = models.ForeignKey(Message_Manu,on_delete=models.CASCADE, null=True, related_name="message")

    def __str__(self):
        return str(self.pk)+ str(".") + str(self.USer)

# all backend orders
class Backend_Order(models.Model):
    USer = models.ForeignKey(User,default=None,on_delete=models.CASCADE,related_name='user_backend_order')
    Service_Type = models.CharField(max_length=250, null=True)
    Backend_Price = models.CharField(max_length=250, null=True)
    Number_Of_Section = models.CharField(max_length=250, null=True)

    Per_section_Price = models.CharField(max_length=250, null=True)

    Website_Functionality = models.CharField(max_length=50, null=True)
    Email = models.EmailField(max_length=50, null=True)

    Project_File = models.FileField(upload_to="1_backend_files/", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    order_message = models.ForeignKey(Message_Manu,on_delete=models.CASCADE, null=True, related_name="message2")

    def __str__(self):
        return str(self.pk)+ str(".") + str(self.USer)


# all complete websites orders
class Complete_Website_Orders(models.Model):
    USer = models.ForeignKey(User,default=None,on_delete=models.CASCADE,related_name='user_complete_website_order')
    Service_Type = models.CharField(max_length=250, null=True)
    Price = models.CharField(max_length=250, null=True)
    Number_Of_Section = models.CharField(max_length=250, null=True)
    Per_section_Price = models.CharField(max_length=250, null=True)
    Website_Functionality = models.CharField(max_length=50, null=True)
    Email = models.EmailField(max_length=50, null=True)
    Project_File = models.FileField(upload_to="2_complete_website_files/", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    order_message = models.ForeignKey(Message_Manu,on_delete=models.CASCADE, null=True, related_name="message3")

    def __str__(self):
        return str(self.pk)+ str(".") + str(self.USer)


# hire me form
class Hire_Me(models.Model):
    USer = models.ForeignKey(User,default=None,on_delete=models.CASCADE, related_name="hireME")
    EMail = models.EmailField(max_length=50, null=True)
    Service_Type = models.CharField(max_length=1, null=True)
    Project_Plan = models.TextField(max_length=250)
    Demo_File = models.FileField(upload_to="4_hire_me/",null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.pk)+ str(".") + str(self.USer)


#profile picture
class Profile_picture(models.Model):
    USer = models.ForeignKey(User,default=None,on_delete=models.CASCADE, related_name="user_propic")
    Profile_picture = models.ImageField(upload_to="3_profile_picture/", null=True, blank=True)

    def __str__(self):
        return str(self.pk)+ str(".") + str(self.USer)

    def get_my_profile(self):
        return self.post_set.all()


#frontend ratings
class Frontend_Rating(models.Model):
    USer = models.OneToOneField(User,default=None,on_delete=models.CASCADE, related_name="frontend_rating")
    Rating = models.IntegerField(null=True)
    Feedback = models.TextField(max_length=250, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.pk)+ str(".") + str(self.USer) + str("(") + str(self.Rating) + str("stars") +str(")")


#backend ratings
class Backend_Rating(models.Model):
    USer = models.OneToOneField(User,default=None,on_delete=models.CASCADE, related_name="backend_rating")
    Rating = models.IntegerField(null=True)
    Feedback = models.TextField(max_length=250, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.pk)+ str(".") + str(self.USer) + str("(") + str(self.Rating) + str("stars") +str(")")

#complete website ratings
class Complete_Website_Rating(models.Model):
    USer = models.OneToOneField(User,default=None,on_delete=models.CASCADE, related_name="complete_website_rating")
    Rating = models.IntegerField(null=True)
    Feedback = models.TextField(max_length=250, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.pk)+ str(".") + str(self.USer) + str("(") + str(self.Rating) + str("stars") +str(")")

class FAQ(models.Model):
    Question = models.CharField(max_length=250, blank=True, null=True)
    Answer = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(User,default=None,null=True, related_name="faqLIKES")

    def __str__(self):
        return str(self.pk) + str(".") + str(self.Question)
