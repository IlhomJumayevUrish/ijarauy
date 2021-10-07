from django.contrib import admin
from parler.admin import TranslatableAdmin
from app.models import Rasmlar, Uylar, Tumanlar,UserData

admin.site.register(Rasmlar)
class ProductImageAdmin(admin.TabularInline):
    model=Rasmlar
@admin.register(Tumanlar)
class FactAdmin(TranslatableAdmin):
    list_display=['name']



@admin.register(UserData)
class UserD(admin.ModelAdmin):
    list_display=['name']

@admin.register(Uylar)
class UyAdmin(TranslatableAdmin):
    list_display=['manzil','xona_soni','narx']
    inlines=[ProductImageAdmin]

