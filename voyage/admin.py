from django.contrib import admin
from . models import Destination,Voyage,Excursion,Client,Reservation

# Register your models here.
admin.site.register(Destination)
admin.site.register(Voyage)
admin.site.register(Excursion)



#admin.site.register(Client)
#admin.site.register(Reservation)

class ReservationInline(admin.TabularInline):
    model = Reservation
    fieldsets =[
            (None, {'fields': ['voyage','traitement']})
        ]
    extra =0

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines =[ReservationInline,]



