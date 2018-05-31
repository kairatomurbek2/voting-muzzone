from django.contrib import messages
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import FormView

from main.utils import get_client_ip
from web.decorators import get_poll, get_choice, check_vote_permisson
from web.form import PollAnswerCheatForm
from web.models import PollAnswer, Poll, Ad


@csrf_exempt
@require_http_methods(["POST"])
@get_poll
@get_choice
@check_vote_permisson
def vote(request, **kwargs):
    PollAnswer.objects.create(choices=kwargs.get('choice'), ip_address=kwargs.get('ip_address'),
                              user_agent=kwargs.get('user_agent'))
    choice = kwargs.get('poll').get_result().filter(id=kwargs.get('choice').id)[0]
    return JsonResponse(
        {'success': True, 'message': 'Спасибо за ваш голос!', 'percent': choice.percent, 'id': choice.id})


def feed(request):
    poll = Poll.objects.filter(is_active=True).last()
    ad = Ad.objects.last()
    data = {}
    page = request.GET.get('page', 1)
    if ad:
        data['ad'] = ad
    if poll:
        choices = Paginator(poll.get_result(), 10)
        data['poll'] = poll
        data['choices'] = choices.get_page(page)
        data['count'] = choices.count
    if request.is_ajax():
        return render(request, 'paginate.html', data)
    return render(request, 'index.html', data)


@csrf_exempt
@require_http_methods(["POST"])
@check_vote_permisson
def check(request, **kwargs):
    return JsonResponse({'success': True, 'message': 'Вы можете проголосовать'})


class PollAnswerCheatView(FormView):
    template_name = 'admin/admin_poll_anwer_cheat.html'
    form_class = PollAnswerCheatForm
    success_url = reverse_lazy('admin:admin_poll_answer_cheat')

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Вы успешно создали!")
        return reverse_lazy('admin:admin_poll_answer_cheat')

    def form_valid(self, form):
        poll_choice = form.cleaned_data['poll_choice']
        count = form.cleaned_data['count']
        user_agent = self.request.META['HTTP_USER_AGENT']
        ip_address = get_client_ip(self.request)
        PollAnswer.objects.bulk_create(
            [PollAnswer(choices=poll_choice, ip_address=ip_address, user_agent=user_agent) for i in range(0, count)])

        return super(PollAnswerCheatView, self).form_valid(form)
