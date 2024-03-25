from django.shortcuts import render, redirect

from wss_app.accounts.forms import ProfileForm


def sign_in(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')

    else:
        form = ProfileForm()

    context = {'form': form,
               }

    return render(request, 'accounts/sign-in-page.html', context=context)


