from django.contrib import admin
from .models import (
    contacts, Frontend_Order,
    Backend_Order,
    Complete_Website_Orders,
    Hire_Me,Message_Manu,
    Profile_picture,
    Frontend_Rating,
    Backend_Rating,
    Complete_Website_Rating,
    FAQ
    )

# Register your models here.
admin.site.register(contacts)
admin.site.register(Hire_Me)
admin.site.register(Message_Manu)
admin.site.register(Profile_picture)

#order purpose
admin.site.register(Frontend_Order)
admin.site.register(Backend_Order)
admin.site.register(Complete_Website_Orders)

#ratings purpose
admin.site.register(Frontend_Rating)
admin.site.register(Backend_Rating)
admin.site.register(Complete_Website_Rating)

#FAQ
admin.site.register(FAQ)
