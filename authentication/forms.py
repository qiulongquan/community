from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import User

def forbidden_username_validator(value):
    """
    用户名禁用词
    """
    forbidden_usernames = {
        'admin', 'settings', 'news', 'about', 'help', 'signin', 'signup',
        'signout', 'terms', 'privacy', 'cookie', 'new', 'login', 'logout',
        'administrator', 'join', 'account', 'username', 'root', 'blog',
        'authentication', 'users', 'billing', 'subscribe', 'reviews', 'review', 'blog',
        'blogs', 'edit', 'mail', 'email', 'home', 'job', 'jobs', 'contribute',
        'newsletter', 'shop', 'profile', 'register', 'authentication', 'authentication',
        'campaign', '.env', 'delete', 'remove', 'forum', 'forums',
        'download', 'downloads', 'contact', 'blogs', 'feed', 'feeds', 'faq',
        'intranet', 'log', 'registration', 'search', 'explore', 'rss',
        'support', 'status', 'static', 'media', 'setting', 'css', 'js',
        'follow', 'activity', 'questions', 'articles', 'network',
    }
    if value.lower() in forbidden_usernames:
        raise ValidationError('This is a reserved word.')

def invalid_username_validator(value):
    """
    检查用户名是否包含非法字符
    """
    if '@' in value or '+' in value or '-' in value:
        msg = _('Enter a valid username.')
        raise ValidationError(msg)


def unique_email_validator(value):
    """
    邮箱唯一性
    """
    if User.objects.filter(email__iexact=value).exists():
        msg = _('User with this Email already exists.')
        raise ValidationError(msg)


def unique_username_ignore_case_validator(value):
    """
    用户名唯一性
    """
    if User.objects.filter(username__iexact=value).exists():
        msg = _('User with this Username already exists.')
        raise ValidationError(msg)


class SignUpForm(forms.ModelForm):
    """
    A form for creating new users.
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,required=True,label=_('Username'),
        help_text=_("Username may contain alphanumeric, '_' and '.' characters.")
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label=_('Password'),required=True
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label=_('Confirm your password'),required=True,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True,max_length=75,label=_('Email')
    )

    class Meta:
        model = User
        exclude = ['last_login', 'date_joined']
        fields = ['username', 'email','password', 'confirm_password',]


    def __init__(self, *args, **kwargs):
        """
        验证表单数据合法性
        """
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators += [
            forbidden_username_validator, invalid_username_validator,
            unique_username_ignore_case_validator,
        ]
        self.fields['email'].validators += [
            unique_email_validator,
        ]

    def clean_password(self):
        '''
        验证两次输入密码是否一致
        '''
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            msg = _('Passwords don\'t match.')
            raise ValidationError(msg)
        return password

    def save(self, commit=True):
        """
        保存前的操作
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user