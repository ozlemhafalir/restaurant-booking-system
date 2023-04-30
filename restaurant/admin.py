from django.contrib import admin

from restaurant.models import Restaurant, RestaurantImage, Table


class TableInline(admin.TabularInline):
    model = Table


class RestaurantImageInline(admin.TabularInline):
    model = RestaurantImage


class RestaurantAdmin(admin.ModelAdmin):
    inlines = [
        TableInline,
        RestaurantImageInline
    ]


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantImage)
admin.site.register(Table)
