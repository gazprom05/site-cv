from django.contrib import admin
from mainapp.models import MenuCategoryTable, EducationTable, CareerTable, AddEducationTable, CertificatesTable

# Register your models here.
admin.site.register(MenuCategoryTable)
admin.site.register(EducationTable)
admin.site.register(CareerTable)
admin.site.register(AddEducationTable)
admin.site.register(CertificatesTable)
