from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Count
from django.core.paginator import Paginator

from web.decorators import get_poll, get_choice, check_vote_permisson
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
    return JsonResponse({'success': True, 'message': 'Спасибо за ваш голос!', 'percent': choice.percent, 'id': choice.id})


def feed(request):
    poll = Poll.objects.filter(is_active=True).last()
    ad = Ad.objects.last()
    data = {}
    page = request.GET.get('page', 1)
    if ad:
        data['ad'] = ad
    if poll:
        choices = Paginator(poll.get_result(), 2)
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