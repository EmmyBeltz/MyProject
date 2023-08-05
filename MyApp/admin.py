from django.contrib import admin

# Register your models here.
from .models import TheWebsiteInfo
from .models import TheWebsiteAboutText
from .models import TheWebsiteImages
from .models import TheWebsiteTrainers
from .models import TheWebsiteCourses
from .models import TheWebsitePricing
from .models import TheWebsiteTestimonials

admin.site.register(TheWebsiteInfo)
admin.site.register(TheWebsiteAboutText)
admin.site.register(TheWebsiteImages)
admin.site.register(TheWebsiteTrainers)
admin.site.register(TheWebsiteCourses)
admin.site.register(TheWebsitePricing)
admin.site.register(TheWebsiteTestimonials)
