from django.shortcuts import render
from wss_app.common.profile_helper import get_profile


def index(request):
    profile = get_profile()
    context = {'profile': profile}

    return render(request, template_name='common/index.html', context=context)


def objective_page(request):
    profile = get_profile()
    context = {'profile': profile}

    return render(request, template_name='common/objective.html', context=context)


