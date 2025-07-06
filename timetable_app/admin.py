from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Member, Trainer, Utilization

# Custom form for creating a new Member
class MemberCreationForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# Custom form for changing an existing Member
class MemberChangeForm(UserChangeForm):
    class Meta:
        model = Member
        fields = ('email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the password field read-only
        self.fields['password'].widget.attrs['readonly'] = True

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        # Only hash if password changed and not already hashed
        if password and password != user.password:
            user.set_password(password)
        if commit:
            user.save()
        return user

# Custom admin for Member
class MemberAdmin(UserAdmin):
    add_form = MemberCreationForm
    form = MemberChangeForm
    model = Member
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

# Register models
admin.site.register(Member, MemberAdmin)
admin.site.register(Trainer)
admin.site.register(Utilization)



