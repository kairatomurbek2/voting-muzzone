
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils.timezone import now

from web.models import Poll, PollChoice, PollAnswer
from main.utils import get_client_ip


def get_poll(func):
    def wrapper(request, poll_id, *args, **kwargs):
        poll = get_object_or_404(Poll, id=poll_id)
        kwargs['poll'] = poll
        if not poll.opportunity_vote:
            return JsonResponse({'success': False, 'message': 'Вы не можете голосовать'})
        return func(request, *args, **kwargs)
    return wrapper


def get_choice(func):
    def wrapper(request, *args, **kwargs):
        choice = request.POST.get('choice')
        if not choice:
            return JsonResponse({'success': False, 'message': 'choice is require'})
        choice = get_object_or_404(PollChoice, id=choice)
        kwargs['choice'] = choice
        return func(request, *args, **kwargs)
    return wrapper


def check_vote_permisson(func):
    def wrapper(request, *args, **kwargs):
        user_agent = request.META['HTTP_USER_AGENT']
        ip_address = get_client_ip(request)
        answer = PollAnswer.objects.filter(choices__poll=kwargs.get('poll'), ip_address=ip_address).last()
        kwargs['ip_address'] = ip_address
        kwargs['user_agent'] = user_agent
        if not answer:
            return func(request, *args, **kwargs)
        current_date = now().replace(tzinfo=None)
        diff = current_date - answer.created_at.replace(tzinfo=None)
        days, seconds = diff.days, diff.seconds
        hours = days * 24 + seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        time = '%sчас %sминут %sсекунд'
        if hours >= 2:
            return func(request, *args, **kwargs)
        elif hours == 0:
            time = time % (1, 59 - minutes, 59 - seconds)
        else:
            time = time % (0, 59 - minutes, 59 - seconds)
        return JsonResponse({'success': False, 'message': 'Вы можете проголосовать через {0}'.format(time)})

    return wrapper