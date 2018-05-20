from django.contrib import admin

from web.models import Poll, PollChoice, PollAnswer, Ad

admin.site.register(Poll)
admin.site.register(PollChoice)
admin.site.register(PollAnswer)
admin.site.register(Ad)
