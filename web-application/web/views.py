from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Count

from web.decorators import get_poll, get_choice, check_vote_permisson
from web.models import PollAnswer, Poll


@csrf_exempt
@require_http_methods(["POST"])
@get_poll
@get_choice
@check_vote_permisson
def vote(request, **kwargs):
    PollAnswer.objects.create(choices=kwargs.get('choice'), ip_address=kwargs.get('ip_address'),
                              user_agent=kwargs.get('user_agent'))

    return JsonResponse({'success': True, 'message': 'Спасибо за ваш голос!'})


def feed(request):
    poll = Poll.objects.filter(is_active=True).last()
    if poll:
        return render(request, 'base.html', {'choices': poll.get_result()})
    else:
        return render(request, 'test.html')

@csrf_exempt
@require_http_methods(["POST"])
@check_vote_permisson
def check(request, **kwargs):
    return JsonResponse({'success': True, 'message': 'Вы можете проголосовать'})