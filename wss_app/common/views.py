from django.shortcuts import render


def index(request):
    # profile = Profile.objects.first()
    context = {}

    return render(request, template_name='common/index.html', context=context)
