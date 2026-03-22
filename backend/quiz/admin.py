from django.contrib import admin
from .models import Question, Session, Badge, UserBadge


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "category", "difficulty")
    search_fields = ("text", "category")
    list_filter = ("category", "difficulty")


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("user", "score", "total_questions", "category", "difficulty", "played_at")
    list_filter = ("category", "difficulty", "played_at")
    search_fields = ("user__username",)


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ("slug", "name", "icon")
    search_fields = ("slug", "name")


@admin.register(UserBadge)
class UserBadgeAdmin(admin.ModelAdmin):
    list_display = ("user", "badge", "unlocked_at")
    search_fields = ("user__username", "badge__slug")
