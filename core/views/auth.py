from django.db import transaction
from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from core.models import User
from core.forms import SignupForm
from core.tasks import activate_user_account
from core.tokens import account_activation_token


@transaction.atomic
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            to_email = form.cleaned_data.get('email')
            message = render_to_string('Auth/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': user.pk,
                'token': account_activation_token.make_token(user),
            })
            activate_user_account.delay(message, to_email)
            return render(
                request,
                'Auth/confirm_email.html',
                {'first_name': user.first_name, 'last_name': user.last_name}
            )
    else:
        form = SignupForm()
    return render(request, 'Auth/signup.html', {'form': form})


def activate_user(request, uid, token):
    try:
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('dashboard')
    else:
        return HttpResponse('Activation link is invalid!')
