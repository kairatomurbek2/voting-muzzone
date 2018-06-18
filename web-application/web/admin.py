from django.conf.urls import url
from django.contrib import admin

from web.models import Poll, PollChoice, PollAnswer, Ad
from web.views import PollAnswerCheatView


class AdminPollAnswer(admin.ModelAdmin):
    def get_urls(self):
        urls = super(AdminPollAnswer, self).get_urls()
        custom_urls = [
            url(r'^admin_poll_answer_cheat/$', self.admin_site.admin_view(self.admin_poll_answer_cheat),
                name='admin_poll_answer_cheat')

        ]
        return custom_urls + urls

    def admin_poll_answer_cheat(self, request):
        return PollAnswerCheatView.as_view()(request)


class PollChoiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'answer_count')

    def answer_count(self, obj):
        return obj.answers.all().count()

    answer_count.short_description = 'Количество голосов'


admin.site.register(Poll)
admin.site.register(PollChoice, PollChoiceAdmin)
admin.site.register(PollAnswer, AdminPollAnswer)
admin.site.register(Ad)
