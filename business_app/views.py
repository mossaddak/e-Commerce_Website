from email import message
from itertools import count
from typing_extensions import Self
from django.shortcuts import get_object_or_404, render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from .models import (
    contacts,
    Frontend_Order,
    Backend_Order,
    Complete_Website_Orders,
    Hire_Me,
    User,
    Profile_picture,
    Frontend_Rating,
    Backend_Rating,
    Complete_Website_Rating,
    FAQ,
    )
from .forms import (
    cnge_profile,
    change_profile_info,
)



#index
def index(request):
    #total_user = User.objects.count()-1
    ALLusers = User.objects.filter(is_superuser=False)
    total_user = ALLusers.count()
    
    profile = Profile_picture.objects.all()


    #order purpose_________________________________________________________________________
    total_user_frontend_orders = Frontend_Order.objects.filter(USer=request.user.id).count()
    total_user_backend_order = Backend_Order.objects.filter(USer=request.user.id).count()
    total_user_complete_website_order = Complete_Website_Orders.objects.filter(USer=request.user.id).count()

    #total orders
    total_user_orders = total_user_frontend_orders+total_user_backend_order+total_user_complete_website_order
    
    
    
    #frontend ratings_______________________________________
    frontend_all_ratings = Frontend_Rating.objects.all()
    number_of_frontend_rating = frontend_all_ratings.count()
    frontend_rating_list = []
    total_ratings = 0
    average_rating = 0

    all_frontend_one_star = all_frontend_two_star = all_frontend_three_star = all_frontend_four_star = all_frontend_five_star =0
    frontend_one_star = frontend_two_star = frontend_three_star = frontend_four_star = frontend_five_star = 0


    if number_of_frontend_rating !=0:
        all_frontend_one_star = Frontend_Rating.objects.filter(Rating=1).count()
        all_frontend_two_star = Frontend_Rating.objects.filter(Rating=2).count()
        all_frontend_three_star = Frontend_Rating.objects.filter(Rating=3).count()
        all_frontend_four_star = Frontend_Rating.objects.filter(Rating=4).count()
        all_frontend_five_star = Frontend_Rating.objects.filter(Rating=5).count()
        

        frontend_one_star = round((Frontend_Rating.objects.filter(Rating=1).count() / number_of_frontend_rating)*100,1)
        frontend_two_star = round((Frontend_Rating.objects.filter(Rating=2).count() / number_of_frontend_rating)*100,1)
        frontend_three_star = round((Frontend_Rating.objects.filter(Rating=3).count() / number_of_frontend_rating)*100,1)
        frontend_four_star = round((Frontend_Rating.objects.filter(Rating=4).count() / number_of_frontend_rating)*100,1)
        frontend_five_star = round((Frontend_Rating.objects.filter(Rating=5).count() / number_of_frontend_rating)*100,1)


    
    for frontend_rating_item in frontend_all_ratings:
        frontend_rating = frontend_rating_item.Rating

        if frontend_rating:
            total_ratings += frontend_rating
            average_rating = round(total_ratings/frontend_all_ratings.count(),1)
            

    #backend ratings______________________________________
    backend_all_ratings = Backend_Rating.objects.all()
    number_of_backend_rating = backend_all_ratings.count()

    total_backend_ratings = average_backend_rating = 0

    all_backend_one_star = all_backend_two_star = all_backend_three_star = all_backend_four_star = all_backend_five_star = 0
    backend_one_star = backend_two_star = backend_three_star = backend_four_star = backend_five_star = 0


    if number_of_backend_rating !=0:
        all_backend_one_star = Backend_Rating.objects.filter(Rating=1).count()
        all_backend_two_star = Backend_Rating.objects.filter(Rating=2).count()
        all_backend_three_star = Backend_Rating.objects.filter(Rating=3).count()
        all_backend_four_star = Backend_Rating.objects.filter(Rating=4).count()
        all_backend_five_star = Backend_Rating.objects.filter(Rating=5).count()
        

        backend_one_star = round((Backend_Rating.objects.filter(Rating=1).count() / number_of_backend_rating)*100,1)
        backend_two_star = round((Backend_Rating.objects.filter(Rating=2).count() / number_of_backend_rating)*100,1)
        backend_three_star = round((Backend_Rating.objects.filter(Rating=3).count() / number_of_backend_rating)*100,1)
        backend_four_star = round((Backend_Rating.objects.filter(Rating=4).count() / number_of_backend_rating)*100,1)
        backend_five_star = round((Backend_Rating.objects.filter(Rating=5).count() / number_of_backend_rating)*100,1)

    for backend_rating_item in backend_all_ratings:
        backend_rating = backend_rating_item.Rating

        if backend_rating:
            total_backend_ratings += backend_rating
            average_backend_rating = round(total_backend_ratings/backend_all_ratings.count(),1)


    
    #complete website ratings_______________________________________________
    complete_website_all_ratings = Complete_Website_Rating.objects.all()
    number_of_complete_website_rating = complete_website_all_ratings.count()

    total_complete_website_ratings = average_complete_website_rating = 0

    all_complete_website_one_star = all_complete_website_two_star = all_complete_website_three_star = all_complete_website_four_star = all_complete_website_five_star = 0
    complete_website_one_star = complete_website_two_star = complete_website_three_star = complete_website_four_star = complete_website_five_star = 0



    if number_of_complete_website_rating !=0:
        all_complete_website_one_star = Complete_Website_Rating.objects.filter(Rating=1).count()
        all_complete_website_two_star = Complete_Website_Rating.objects.filter(Rating=2).count()
        all_complete_website_three_star = Complete_Website_Rating.objects.filter(Rating=3).count()
        all_complete_website_four_star = Complete_Website_Rating.objects.filter(Rating=4).count()
        all_complete_website_five_star = Complete_Website_Rating.objects.filter(Rating=5).count()
        

        complete_website_one_star = round((Complete_Website_Rating.objects.filter(Rating=1).count() / number_of_complete_website_rating)*100,1)
        complete_website_two_star = round((Complete_Website_Rating.objects.filter(Rating=2).count() / number_of_complete_website_rating)*100,1)
        complete_website_three_star = round((Complete_Website_Rating.objects.filter(Rating=3).count() / number_of_complete_website_rating)*100,1)
        complete_website_four_star = round((Complete_Website_Rating.objects.filter(Rating=4).count() / number_of_complete_website_rating)*100,1)
        complete_website_five_star = round((Complete_Website_Rating.objects.filter(Rating=5).count() / number_of_complete_website_rating)*100,1)

    for complete_website_rating_item in complete_website_all_ratings:
        complete_website_rating = complete_website_rating_item.Rating

        if complete_website_rating:
            total_complete_website_ratings += complete_website_rating
            average_complete_website_rating = round(total_complete_website_ratings/complete_website_all_ratings.count(),1)




    if request.user.is_authenticated:
        frontend_order_list = request.user.user_frontend_order.all()
        backend_order_list = request.user.user_backend_order.all()
        Complete_Website_Order_list = request.user.user_complete_website_order.all()

        #rating purpose
    else:
        frontend_order_list = Frontend_Order.objects.none()
        backend_order_list = Backend_Order.objects.none()
        Complete_Website_Order_list = Complete_Website_Orders.objects.none()


    #FAQ likes
    allFAQ =  FAQ.objects.all()

    

    context = {
        "all":all,
        "total_user_orders":total_user_orders,
        "total_user":total_user,
        "frontend_order_list":frontend_order_list,
        "backend_order_list":backend_order_list,
        "Complete_Website_Order_list":Complete_Website_Order_list,
        "profile":profile,
        "number_of_frontend_rating":number_of_frontend_rating,
        "frontend_rating_list":frontend_rating_list,
        "total_ratings":total_ratings,
        "average_rating":average_rating,
        "ALLusers":ALLusers,

        #frontend ratings________________________
        "frontend_all_ratings":frontend_all_ratings,

        "all_frontend_one_star":all_frontend_one_star,
        "all_frontend_two_star":all_frontend_two_star,
        "all_frontend_three_star":all_frontend_three_star,
        "all_frontend_four_star":all_frontend_four_star,
        "all_frontend_five_star":all_frontend_five_star,

        "frontend_one_star":frontend_one_star,
        "frontend_two_star":frontend_two_star,
        "frontend_three_star":frontend_three_star,
        "frontend_four_star":frontend_four_star,
        "frontend_five_star":frontend_five_star,

        #backend ratings___________________________
        "backend_all_ratings":backend_all_ratings,
        "number_of_backend_rating":number_of_backend_rating,
        "average_backend_rating":average_backend_rating,

        "all_backend_one_star":all_backend_one_star,
        "all_backend_two_star":all_backend_two_star,
        "all_backend_three_star":all_backend_three_star,
        "all_backend_four_star":all_backend_four_star,
        "all_backend_five_star":all_backend_five_star,

        "backend_one_star":backend_one_star,
        "backend_two_star":backend_two_star,
        "backend_three_star":backend_three_star,
        "backend_four_star":backend_four_star,
        "backend_five_star":backend_five_star,


        #complete website ratings___________________________
        "complete_website_all_ratings":complete_website_all_ratings,
        "number_of_complete_website_rating":number_of_complete_website_rating,
        "average_complete_website_rating":average_complete_website_rating,

        "all_complete_website_one_star":all_complete_website_one_star,
        "all_complete_website_two_star":all_complete_website_two_star,
        "all_complete_website_three_star":all_complete_website_three_star,
        "all_complete_website_four_star":all_complete_website_four_star,
        "all_complete_website_five_star":all_complete_website_five_star,

        "complete_website_one_star":complete_website_one_star,
        "complete_website_two_star":complete_website_two_star,
        "complete_website_three_star":complete_website_three_star,
        "complete_website_four_star":complete_website_four_star,
        "complete_website_five_star":complete_website_five_star,

        #faq
        "allFAQ":allFAQ,
        







    }
    return render(request,'0_index.html',context)


#create account 
def handle_singUp(request):
    if request.method == "POST":
        userName = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        

        if pass1 != pass2:
            messages.error(request,"Passwords aren't matching! Please try again!")
            return redirect("/") 
        else:
                    
            try:
                myUser = User.objects.create_user(userName,email,pass1)
                myUser.first_name = fname
                myUser.last_name = lname
                
                myUser.save()
                messages.success(request,"Your account has been created!")
                return redirect("/") 
            except:
                messages.error(request,"The username already exist!")
                return redirect("/") 
                    
    else:
        return HttpResponse("404-Not found the page")


      
#login account
def handle_login(request):
    if request.method == "POST":
        loginUserName = request.POST['loginUserName']
        Loginpass = request.POST['Loginpass']

        user = authenticate(username = loginUserName,password = Loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,f"welcome {user.first_name}. You can order any Kind of websie you required!")
            return redirect("/")
        else:
            messages.error(request,"You don't have any account,Please create an account!")
            return redirect("/")

    return redirect("/")


#logout account
def handle_logout(request):
    logout(request)
    messages.success(request,"You successfully logout!")
    return redirect("/")


#hire me
def hire_me(request):
    
    if request.user.is_authenticated:
        if request.method == "POST":
            service_type = request.POST.get('service_type')
            service_plan = request.POST.get('project_Plan')
            demo_file = request.FILES['frontend_file'] if 'frontend_file' in request.FILES else None
        
            Hire_Me.objects.create(
                Service_Type = service_type,
                Project_Plan = service_plan,
                Demo_File = demo_file,
                USer = request.user,
                EMail = request.user.email
                )        
            messages.success(request,f"{request.user.first_name}, Your request is sent.I'll contact you very soon.")
            
            return redirect("/")

    return render(request,"index.html", {})


#all frontend orders
def frontend_orders(request):
    if request.user.is_authenticated:
    
        if request.method == "POST":
            frontend_orders_request = request.FILES['frontend_file'] if 'frontend_file' in request.FILES else None
            sections = request.POST.get('numField11')
            functionality = request.POST.get('frontend')
            service_type = "Frontend"
            per_section_price = 0

            if functionality == "Portfolio":
                price = f"${int(sections)*10}"
                per_section_price = "$10"
            elif (functionality == "e-Commerce") or (functionality == "Social Media"):
                price = f"${int(sections)*15}"
                per_section_price = "$15"
            
            Frontend_Order.objects.create(
                files = frontend_orders_request,
                Service_Type = service_type,
                Number_of_Section = sections,
                Website_Functionality = functionality,
                Price = price,
                USer = request.user,
                Email = request.user.email,
                Per_section_Price = per_section_price
                )

            messages.success(request,f"{request.user.first_name}, Your order is procecing. I'll cotact you before placing the order.")
            
            return redirect("/", userz = request.user)
    else:
        messages.error(request,"Please login or create an account.")
   
    return redirect("/")


#all backend orders
def backend_orders(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            backend_orders_demo_project_file = request.FILES['backend_file'] if 'backend_file' in request.FILES else None
            sections = request.POST.get('backend_num_field')
            functionality = request.POST.get('backend_functionaliy')
            service_type = "Backend"
            per_section_price = 0

            if functionality == "Portfolio":
                price = f"${int(sections)*10}"
                per_section_price = "$10"
            elif (functionality == "e-Commerce") or (functionality == "Social Media"):
                price = f"${int(sections)*15}"
                per_section_price = "$15"


            Backend_Order.objects.create(
                USer = request.user,
                Service_Type = service_type,
                Backend_Price = price,
                Number_Of_Section = sections,
                Website_Functionality = functionality,
                Email = request.user.email,
                Project_File = backend_orders_demo_project_file,
                Per_section_Price = per_section_price 
                )
           

            messages.success(request,f"{request.user.first_name}, Your order is procecing. I'll cotact you before placing the order.")
            
            return redirect("/", userz = request.user)

    
    else:
        messages.error(request,"Please login or create an account.")
   
    return redirect("/")


#all complete orders
def complete_website_orders(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            backend_orders_demo_project_file = request.FILES['complete_website_file'] if 'complete_website_file' in request.FILES else None
            sections = request.POST.get('complete_website_num_field')
            functionality = request.POST.get('complete_website')
            service_type = "Complete Website"
            per_section_price = 0

            if functionality == "Portfolio":
                price = f"${int(sections)*20}"
                per_section_price = "$20"
            elif (functionality == "e-Commerce") or (functionality == "Social Media"):
                price = f"${int(sections)*30}"
                per_section_price = "$30"



            Complete_Website_Orders.objects.create(
                USer = request.user,
                Service_Type = service_type,
                Price = price,
                Number_Of_Section = sections,
                Website_Functionality = functionality,
                Email = request.user.email,
                Project_File = backend_orders_demo_project_file,
                Per_section_Price = per_section_price 
                )
           

            messages.success(request,f"{request.user.first_name}, Your order is procecing. I'll cotact you before placing the order.")
            
            return redirect("/", userz = request.user)

    
    else:
        messages.error(request,"Please login or create an account.")
   
    return redirect("/")




#handaling contact
def handle_contact(request):

    if request.method == "POST":

        contact = contacts()
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')

        contact.name = name
        contact.email = email
        contact.text = text
        contact.save()
        messages.success(request,"Thanks for messaging. I will contact you very soon through.")

        #return HttpResponse("Done")
        
    return redirect('/')




#frontend order information
def frontend_order_details(request, frontend_order_id):
    frontend_order_details = Frontend_Order.objects.get(pk=frontend_order_id)

    context = {
        "frontend_order_details":frontend_order_details,
    }

    return render(request, '21_frontend_order_details.html', context)


#backend order information
def backend_order_details(request, backend_order_id):
    backend_order_details = Backend_Order.objects.get(pk=backend_order_id)

    context = {
        "backend_order_details":backend_order_details,
    }

    return render(request, '22_backend_order_details.html', context)



#complete website order information
def complete_website_order_details(request, complete_website_order_id):
    complete_website_order_details = Complete_Website_Orders.objects.get(pk=complete_website_order_id)

    context = {
        "complete_website_order_details":complete_website_order_details,
    }

    return render(request, '23_complete_website_order_details.html', context)



def user_profile(request, user_id):

    account = get_object_or_404(User, pk = request.user.pk)

    context = {
        "account":account
    }

    return render(request,'0_index.html', context)

#change profile picture
def change_profile_picture(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            profile_picture = request.FILES['profile_picture'] if 'profile_picture' in request.FILES else None

            user = get_object_or_404(User, pk=request.user.pk)
            if request.user.pk != user.pk:
                messages.success(request,f"{request.user.first_name}, Your profile picture not updated")
                return redirect("/")

            Profile_picture.objects.create(
                Profile_picture = profile_picture,
                USer = request.user,
                )        
            messages.success(request,f"{request.user.first_name}, Your profile picture updated")


            
            return redirect("/")
    return render(request,'0_index.html')



class pp_update(UpdateView):
    model = Profile_picture
    from_class = cnge_profile
    fields = 'Profile_picture',                                                                   
    template_name = '00_pp_change.html'
    success_url =("http://127.0.0.1:8000/")


#frontend order edit
def frontend_order_edit(request,frontend_order_id):
    frontend_order_edit = Frontend_Order.objects.get(pk=frontend_order_id)
    context = {
        "frontend_order_edit":frontend_order_edit,
    }
    
    return render(request, "26_frontend_edit.html", context)

#backend order edit
def backend_order_edit(request,backend_order_id):
    backend_order_edit = Backend_Order.objects.get(pk=backend_order_id)
    context = {
        "backend_order_edit":backend_order_edit,
    }
    
    return render(request, "27_backend_edit.html", context)


#backend order edit
def complete_website_order_edit(request,complete_website_order_id):
    complete_website_order_edit = Complete_Website_Orders.objects.get(pk=complete_website_order_id)
    context = {
        "complete_website_order_edit":complete_website_order_edit,
    }
    
    return render(request, "28_comlete_web_edit.html", context)


#order delete
def frontend_order_delete(request, frontend_order_id):
    Frontend_Order.objects.get(pk=frontend_order_id).delete()
    messages.success(request,f"{request.user.first_name}, Your order succsessfully deleted!")
    return redirect("/")

def backend_order_delete(request, backend_order_id):
    Backend_Order.objects.get(pk=backend_order_id).delete()
    messages.success(request,f"{request.user.first_name}, Your order succsessfully deleted!")
    return redirect("/")

def complete_website_order_delete(request, complete_website_order_id):
    Complete_Website_Orders.objects.get(pk=complete_website_order_id).delete()
    messages.success(request,f"{request.user.first_name}, Your order succsessfully deleted!")
    return redirect("/")


#frontend order rating
def frontend_order_rating(request):
    if request.user.is_authenticated:
 
        if request.method == "POST":
            frontend_rating = int(request.POST.get('frontend_ratting'))
            frontend_feedback = request.POST.get('frontend_feedback')
            
            try:
                Frontend_Rating.objects.create(
                    USer = request.user,
                    Rating = int(frontend_rating),
                    Feedback = frontend_feedback
                    )

                messages.success(request,f"{request.user.first_name}, Thank You for your feedback!")
                
                return redirect("/", userz = request.user)
            except:
                messages.error(request,f"{request.user.first_name}, Sorry! You've already given a feedback!")
                return redirect("/", userz = request.user)

    else:
        messages.error(request,"Please login or create an account.")
   
    return redirect("/")


#backend website rating
def backend_order_rating(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            frontend_rating = int(request.POST.get('backend_ratting'))
            backend_feedback = request.POST.get('backend_feedback')
            f_rattings = 0


            try:
                Backend_Rating.objects.create(
                    USer = request.user,
                    Rating = int(frontend_rating),
                    Feedback = backend_feedback
                    )

                messages.success(request,f"{request.user.first_name}, Thank You for your feedback!")
                
                return redirect("/", userz = request.user)
            except:
                messages.error(request,f"{request.user.first_name}, Sorry! You've already given a feedback!")
                return redirect("/", userz = request.user)
           
        
        

    else:
        messages.error(request,"Please login or create an account.")
   
    return redirect("/")


#complete website rating
def complete_website_order_rating(request):
    if request.user.is_authenticated:
    
        if request.method == "POST":
            complete_website_rating = int(request.POST.get('complete_website_ratting'))
            complete_website_feedback = request.POST.get('complete_website_feedback')

            try:
                Complete_Website_Rating.objects.create(
                    USer = request.user,
                    Rating = int(complete_website_rating),
                    Feedback = complete_website_feedback
                    )

                messages.success(request,f"{request.user.first_name}, Thank You for your feedback!")
                
                return redirect("/", userz = request.user)
            except:
                messages.error(request,f"{request.user.first_name}, Sorry! You've already given a feedback!")
                return redirect("/", userz = request.user)

    else:
        messages.error(request,"Please login or create an account.")
   
    return redirect("/")


#profile information update
class profile_info_update(UpdateView):
    model = User
    from_class = change_profile_info
    fields = 'first_name','last_name','email'                                                                
    template_name = '33_change_profile_info.html'
    success_url =("/")





#like view
def likeView(request,pk):
    post = get_object_or_404(FAQ, id=request.POST.get('faqLIKEid'))
    
    if request.user.is_authenticated:
        post.likes.add(request.user)
        messages.success(request,f" Dear customer you liked {post.pk} number FAQ!")
        return redirect("/")
    
    else:
        messages.error(request,"Dear customer please loged nto your account!")
        return redirect("/")

#unlike
def unlike(request,pk):
    post = FAQ.objects.get(pk=pk)
    post.likes.remove(request.user)

    messages.success(request,f" Dear customer you removed your like from {post.pk} number FAQ!")
    return redirect("/")


