from django.contrib import admin
from .models import LiveStream, VideoLibrary, Donation, CommunityResource


admin.site.register(LiveStream)
admin.site.register(VideoLibrary)
admin.site.register(Donation)
admin.site.register(CommunityResource)

admin.site.site_header = 'Virtual Church Administration Page'
