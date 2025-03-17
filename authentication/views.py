from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.utils.encoding import smart_bytes, smart_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.conf import settings

from authentication.forms import PasswordResetRequestForm, PasswordResetForm


def login_get_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    next_page = request.GET.get('next', '')

    if next_page:
        request.session['next_page'] = next_page

    login_form_data = request.session.get('login_form_data', {})
    errors_login_form = request.session.get('errors_login_form', [])

    if errors_login_form:
        del request.session['errors_login_form']

    form = AuthenticationForm(initial=login_form_data)

    return render(request, 'authentication/login.html', {'form': form, 'errors': errors_login_form})


def login_post_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    next_page = request.session.get('next_page')

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        request.session['login_form_data'] = request.POST

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session.pop('next_page') if next_page else ...
            return redirect(next_page) if next_page else redirect('dashboard:home')
        else:
            request.session['errors_login_form'] = [
                "Credenciais incorretas."
            ]
            return redirect('authentication:login')


def logout_view(request):
    logout(request)
    return redirect('authentication:login')


def password_reset_request_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    if request.method == 'POST':
        form = PasswordResetRequestForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = get_object_or_404(User, email=email)

            uid64 = urlsafe_base64_encode(smart_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)

            current_site = get_current_site(request).domain

            relative_link = reverse('authentication:password_reset', kwargs={'uidb64': uid64, 'token': token})
            absurl = f'http://{current_site}{relative_link}'

            username = user.username

            email_body = f'Olá {username},\n\nPara redefinir sua senha, clique no link abaixo:\n{absurl}'

            send_mail(
                subject='Redefinição de senha',
                message=email_body,
                recipient_list=[user.email],
                from_email=f'SGE <{settings.DEFAULT_FROM_EMAIL}>',
                fail_silently=False
            )

            messages.success(request, 'E-mail de redefinição de senha enviado com sucesso.')

            return redirect('authentication:login')
        else:
            return render(request, 'authentication/password_reset_request.html', {'form': form})

    return render(request, 'authentication/password_reset_request.html')


def password_reset_view(request, uidb64, token):
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    try:
        user_id = smart_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, pk=user_id)
    except (User.DoesNotExist, ValueError, OverflowError):
        messages.error(request, 'Link inválido ou expirado.')
        return redirect('authentication:password_reset_request')

    if not PasswordResetTokenGenerator().check_token(user, token):
        messages.error(request, 'Link inválido ou expirado.')
        return redirect('authentication:password_reset_request')

    if request.method == 'POST':
        form = PasswordResetForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            messages.success(request, 'Senha redefinida com sucesso.')
            return redirect('authentication:login')
        else:
            messages.error(request, 'Erro ao redefinir a senha.')
            return render(request, 'authentication/password_reset.html', {'form': form, 'uidb64': uidb64, 'token': token})
    else:
        form = PasswordResetForm()

        return render(request, 'authentication/password_reset.html', {'form': form, 'uidb64': uidb64, 'token': token})
