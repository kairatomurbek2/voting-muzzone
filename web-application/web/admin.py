from django.conf.urls import url
from django.contrib import admin
from django.contrib.admin import AdminSite

from web.models import Poll, PollChoice, PollAnswer, Ad
from web.views import PollAnswerCheatView


class AdminPollAnswerCheat(AdminSite):
    def get_urls(self):
        urls = super(AdminPollAnswerCheat, self).get_urls()
        custom_urls = [
            url(r'^admin_poll_answer_cheat/$', self.admin_view(self.admin_poll_answer_cheat),
                name='admin_poll_answer_cheat')

        ]
        return custom_urls + urls

    def admin_poll_answer_cheat(self, request):
        return PollAnswerCheatView.as_view()(request)


admin.site = AdminPollAnswerCheat()
admin.site.register(Poll)
admin.site.register(PollChoice)
admin.site.register(PollAnswer)
admin.site.register(Ad)
