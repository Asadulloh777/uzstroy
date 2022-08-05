from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminTur(admin.ModelAdmin):
    list_display = ['id','nomi']

class AdminLoyiha(admin.ModelAdmin):
    list_display = ['id','nomi','rasm','tur','narx','manzil','vaqt']

class AdminMurojat(admin.ModelAdmin):
    list_display = ['id','ism','fam','mail','text','vaqt']

class AdminMurojatbot(admin.ModelAdmin):
    list_display = ['id','ism','fam','mail','text','vaqt']

class AdminObuna(admin.ModelAdmin):
    list_display = ['id','name','pochta']

admin.site.register(Obuna, AdminObuna)
admin.site.register(Murojat, AdminMurojat)
admin.site.register(Murojatbot, AdminMurojatbot)
admin.site.register(Tur,AdminTur)
admin.site.register(Loyiha,AdminLoyiha)