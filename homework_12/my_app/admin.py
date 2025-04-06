from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "created_at")
    list_filter = ("name", "category")
    search_fields = ("name", "category__name")
    date_hierarchy = "created_at"

    actions = ["make_price_100", "make_price_1000"]

    @admin.action(description="Все по 100")
    def make_price_100(self, request, queryset):
        updated = queryset.update(price=100)
        self.message_user(request, f"Цена изменена для {updated} товаров")

    @admin.action(description="Все по 1000")
    def make_price_1000(self, request, queryset):
        updated = queryset.update(price=999.99)
        self.message_user(request, f"Цена изменена для {updated} товаров")
