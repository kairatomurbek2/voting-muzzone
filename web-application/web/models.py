from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import F, Count, FloatField
from django.db.models.functions import Cast

from main.utils import poll_choices_image_path, ad_image_path


class Poll(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Зоголовок'))
    is_active = models.BooleanField(default=True, verbose_name=_('Активный'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('Дата создание'))

    def get_result(self):
        answers_count = PollAnswer.objects.filter(choices__poll=self.id).count()
        return self.choices.annotate(percent=Cast((Count('answers') * 100), FloatField()) / answers_count,
                                     answer_count=Count('answers')).order_by('-percent')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Опрос')
        verbose_name_plural = _('Опросы')


class PollChoice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('Зоголовок'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Описание'))
    image = models.ImageField(upload_to=poll_choices_image_path, verbose_name=u"Изображение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Участник')
        verbose_name_plural = _('Участники')


class PollAnswer(models.Model):
    choices = models.ForeignKey(PollChoice, on_delete=models.CASCADE, verbose_name=_('Вариант'), related_name='answers')
    ip_address = models.GenericIPAddressField(verbose_name=_('Ip адресс'))
    user_agent = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Ответ')
        verbose_name_plural = _('Ответы')


class Ad(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Зоголовок'), blank=True, null=True)
    image = models.ImageField(upload_to=ad_image_path, verbose_name=u"Изображение")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Спонсор')
        verbose_name_plural = _('Спонсоры')
