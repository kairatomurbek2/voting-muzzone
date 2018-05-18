from django.db import models
from django.utils.translation import ugettext_lazy as _

from main.image_utils import poll_choices_image_path

# Create your models here.


class Poll(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Зоголовок'))
    is_active = models.BooleanField(default=True, verbose_name=_('Активный'))
    created_at = models.DateField(auto_now=True, verbose_name=_('Дата создание'))

    class Meta:
        verbose_name = _('Опрос')
        verbose_name_plural = _('Опросы')


class PollChoice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('Зоголовок'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Описание'))
    image = models.ImageField(upload_to=poll_choices_image_path, verbose_name=u"Изображение")

    class Meta:
        verbose_name = _('Участник')
        verbose_name_plural = _('Участники')


class PollAnswer(models.Model):
    choices = models.ForeignKey(PollChoice, on_delete=models.CASCADE, verbose_name=_('Вариант'))
    id_address = models.GenericIPAddressField(verbose_name=_('Ip адресс'))
    user_agent = models.CharField(max_length=200)
    created_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = _('Ответ')
        verbose_name_plural = _('Ответы')
