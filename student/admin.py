from django.contrib import admin
from student.models import sinfoin,act
class showdataset(admin.ModelAdmin):
    list_display=('name','phone','email','password')
admin.site.register(sinfoin,showdataset)

class showact(admin.ModelAdmin):
    display=('name')
admin.site.register(act,showact)
# Register your models here.
