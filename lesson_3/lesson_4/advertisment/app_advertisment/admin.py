from django.contrib import admin
from .models import Advertisement
#
#
 # Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_at', 'auction']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, qeryset):
        qeryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, qeryset):
        qeryset.update(auction=True)



admin.site.register(Advertisement, AdvertisementAdmin)