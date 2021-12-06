from django.contrib import admin
from .models import Project
from blog.models import Blog
from .models import Certificate
from .models import Recommendation

admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(Certificate)
admin.site.register(Recommendation)
