from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordResetConfirmView, PasswordResetView
from django.urls import reverse_lazy
# from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.utils.encoding import force_bytes, force_text
from django.views.generic.base import TemplateView, View

from accounts.forms import AccountForm, LoginForm, PwdResetConfirmForm, PwdResetForm, RegistrationForm
from django.views.generic import CreateView
from django.contrib.auth import get_user_model, login
from accounts.utils.tokens import account_activation_token
from accounts.tasks import send_confirmation_mail
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.views import LogoutView

User = get_user_model()


# Create your views here.

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response


def account_register(request):

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = User(
                email = registerForm.cleaned_data.get('email'),
                first_name = registerForm.cleaned_data.get('first_name'),
                last_name = registerForm.cleaned_data.get('last_name')
            )
            user.set_password(registerForm.cleaned_data["password1"])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = "Activate your Account"
            message = render_to_string(
                "email/confirmation_email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            user.email_user(subject=subject, message=message)
            return render(request, "email/register_email_confirm.html", {"form": registerForm})
    else:
        registerForm = RegistrationForm()
    return render(request, "register.html", {"form": registerForm})


class CustomLogoutView(LogoutView):
    next_page = '/'


def activate(request, uidb64, token):
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.filter(pk=uid, is_active=False).first()

    if user is not None and account_activation_token.check_token(user, token):
        messages.success(request, 'Your profile is activated')
        user.is_active = True
        user.save()
        CustomLogoutView()
        return redirect('accounts:login')
    else:
        messages.error(request, 'Your session is expired')
        return redirect('/')





# Password Reset 

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'password/password_reset_email.html'
    form_class = PwdResetForm
    template_name = 'password/password_reset_form.html'
    success_url="password_reset_email_confirm/"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name   = "password/password-reset-confirm.html"
    # success_url     = "password_reset_complete/"
    success_url     = '/'
    form_class      =  PwdResetConfirmForm


class CustomResetEmailConfirmView(TemplateView):
    template_name   = "password/reset_status.html"


class CustomPasswordResetCompleteView(TemplateView):
    template_name   = "password/reset_status.html"



class AccountView(View):
    template_name = 'account_information.html'
    http_method_names = ['post', 'get']

    def get(self, request):
        form = AccountForm(instance=request.user)
        return render(request, 'account_information.html', {'form': form})

    def post(self, request):
        form = AccountForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=request.user.pk)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            messages.success(request, 'Your profile is updated')
            return redirect('accounts:account')
        else:
            messages.error(request, 'Your profile is not updated')
            return redirect('accounts:account')





def AddressBook(request):
    return render(request, 'address_book.html')
