from django.contrib import admin
from . import models


# Register your models here.
class GroupMemberInline(admin.TabularInline):  # we are using this so that we can edit anything inside parent group page only
    model = models.GroupMember


admin.site.register(models.Group)
