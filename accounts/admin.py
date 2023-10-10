from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from accounts.models import User


# 생성
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        # Form 클래스는 데이터 검증(validation)을 담당
        # 사용자가 웹페이지에서 폼을 제출하면, 해당 데이터는 해당 폼의 clean 메서드를 통해 검증
        # 검증이 완료된 데이터는 cleaned_data 딕셔너리에 저장
        # cleaned_data는 폼 필드의 이름을 키로 사용 => 검증된 데이터를 저장하는 딕셔너리
        # 따라서, self.cleaned_data.get("password1")는:
        # .get("password1"): cleaned_data 딕셔너리에서 "password1"이라는 키로 저장된 값을 반환
        # 만약 "password1"이라는 키로 데이터가 없으면, None을 반환.

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# 내용변경
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "password", "birthday", "name", "is_active", "is_admin"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    # 위에 만들어준 클라스 불러오고
    add_form = UserCreationForm
    # 새로운 유저생길때는 저 클라스 불러오고

    list_display = [
        "email",
        "name",
        "birthday",
        "is_admin",
        "is_active",
    ]  # 목록(list) 페이지에 표시될 필드의 순서를 정의 (fieldset과는 다른)
    list_filter = ["is_admin", "is_active"]
    fieldsets = [
        (None, {"fields": ["email", "password", "name", "birthday"]}),
        ("Permissions", {"fields": ["is_admin", "is_active"]}),
    ]
    #새로추가되는 유저 
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "birthday", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]  # 검색창 추가해주고, 이메일을 넣어준것
    ordering = ["email"]
    filter_horizontal = (
        []
    )  # manytomany 관계의 필드일떄 관련항목을 좀 더 사용자 친화적으로 추가하거나 제거할수있께 위젯설정하는데 사용
    # filter_horizontal 위젯은 왼쪽 박스에 사용 가능한 항목들을, 오른쪽 박스에 선택된 항목들을 표시합니다.
    # 사용자는 두 박스 사이의 화살표 버튼을 사용하여 항목을 추가하거나 제거할 수 있습니다.

admin.site.register(User, UserAdmin)


if Group in admin.site._registry:
    admin.site.unregister(Group)
