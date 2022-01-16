from django import forms

from app.models import BigDepartment, Unit


class DepartmentForm(forms.ModelForm):
    class Meta:
        file = forms.FileField()
        model = BigDepartment
        fields = ['name', 'description', 'image']


class UnitForm(forms.ModelForm):
    class Meta:
        # file = forms.FileField()
        model = Unit
        fields = ['title', 'description', 'image', 'department']
