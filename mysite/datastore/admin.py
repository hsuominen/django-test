# from django.contrib import admin
# from datastore.models import acquisition, coordinate, value

# class CoordinateInline(admin.TabularInline):
#     model = coordinate

# class ValueInline(admin.TabularInline):
#     model = value

# class AcquisitionAdmin(admin.ModelAdmin):
#     fields = ['acqdatetime']
#     list_filter = ['acqdatetime']
#     date_hierarchy = 'acqdatetime'
#     #list_display = ('acqdatetime')

#     inlines = [CoordinateInline,ValueInline]

# admin.site.register(acquisition, AcquisitionAdmin)