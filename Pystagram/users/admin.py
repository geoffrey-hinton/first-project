from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


# Register your models here.

class FollowersInline(admin.TabularInline):
    model = User.following.through
    fk_name = "from_user"
    verbose_name = "People I follow"
    verbose_name_plural =  f"{verbose_name} list"
    extra = 1

class FollowingInline(admin.TabularInline):
    model = User.following.through
    fk_name = "to_user"
    verbose_name = "People who follow me"
    verbose_name_plural = f"{verbose_name} list"
    extra = 1

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # list_display = [
    #     "id",
    #     "username",
    #     "is_staff",
    # ]

    fieldsets = [
        (None, {"fields" : ("username", "password")}),
        ("private", {"fields" : ("first_name", "last_name", "email")}),
        ("add_field", {"fields" : ("profile_image", "short_description")}),
        ("related_objects", {"fields" : ("like_posts",)}),
        (
            "privilege",
            {
                "fields" : (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        ("important_schedule", {"fields" : ("last_login", "date_joined")}),
    ]

    inlines = [
        FollowersInline,
        FollowingInline,
    ]