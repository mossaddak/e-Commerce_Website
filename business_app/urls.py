from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    #singup,lgion,logout
    path('singup', views.handle_singUp, name= "handle_singUp"),
    path('login', views.handle_login, name="handle_login"),
    path('logout', views.handle_logout, name="handle_logout"),

    #contact form
    path('contact', views.handle_contact, name="handle_contact"),

    #storing order
    path('frontend_orders/', views.frontend_orders, name="frontend_orders"),
    path('backend_orders/', views.backend_orders, name="backend_orders"),
    path('complete_website_orders/', views.complete_website_orders, name="complete_website_orders"),

    #storing hire_me form
    path('hire_me', views.hire_me, name="hire_me"),

    #order details
    path('frontend_order_details/<int:frontend_order_id>/', views.frontend_order_details, name="frontend_order_details"),
    path('backend_order_details/<int:backend_order_id>/', views.backend_order_details, name="backend_order_details"),
    path('complete_website_order_details/<int:complete_website_order_id>/', views.complete_website_order_details, name="complete_website_order_details"),

    #profile
    path('user_profile/<int:user_id>/', views.user_profile, name="user_profile"),
    path('change_profile_picture/', views.change_profile_picture, name="change_profile_picture"),
    path('pp_update/<int:pk>', views.pp_update.as_view(), name="pp_update"),

    path('profile_info_update/<int:pk>', views.profile_info_update.as_view(), name="profile_info_update"),

    
    
    

    #for edit
    path('frontend_order_edit/<int:frontend_order_id>/', views.frontend_order_edit, name="frontend_order_edit"),
    path('backend_order_edit/<int:backend_order_id>/', views.backend_order_edit, name="backend_order_edit"),
    path('complete_website_order_edit/<int:complete_website_order_id>/', views.complete_website_order_edit, name="complete_website_order_edit"),

    #for delete
    path('frontend_order_delete/<int:frontend_order_id>/', views.frontend_order_delete, name="frontend_order_delete"),
    path('backend_order_delete/<int:backend_order_id>/', views.backend_order_delete, name="backend_order_delete"),
    path('complete_website_order_delete/<int:complete_website_order_id>/', views.complete_website_order_delete, name="complete_website_order_delete"),

    #rating
    path('frontend_ratings/', views.frontend_order_rating, name="frontend_ratings"),
    path('backend_ratings/', views.backend_order_rating, name="backend_ratings"),
    path('complete_website_rating/', views.complete_website_order_rating, name="complete_website_rating"),


    #like button
    path('like_post/<int:pk>', views.likeView, name="like_post"),
    path('unlike/<int:pk>', views.unlike, name="unlike")

    

]