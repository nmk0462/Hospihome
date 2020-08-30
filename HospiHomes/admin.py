from django.contrib import admin
from .models import User
from .models import User1
from .models import details
from .models import upd
from .models import appt
from .models import approvedapp
from .models import rate
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(User1)
admin.site.register(details)
admin.site.register(upd)
admin.site.register(appt)
admin.site.register(approvedapp)
admin.site.register(rate)