from django.contrib import admin
from .models import *

# Register your models here.
# admin 화면에 post를 볼 수 있도록 한다.
admin.site.register(Post)
admin.site.register(Comment)

class CategoryAdmin(admin.ModelAdmin):
   # prepopulated_fields : 다른 필드의 값을 가지고 와서 자동으로 할당해줌.
   prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, CategoryAdmin)