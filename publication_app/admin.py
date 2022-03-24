from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.contrib.auth.models import User

from .models import Post, Profile

# admin.site.register(Post)

class ProfileInLine(admin.StackedInline):
    model = Profile


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(UserAdminBase):
    inlines = (
        ProfileInLine,
    )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_date', 'title',)
    ordering = ('-create_date', '-id',)
    readonly_fields = ('create_date',)
