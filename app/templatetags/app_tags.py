from django import template

from app.models import BigDepartment

register = template.Library()


@register.simple_tag()
def categories():
    department = BigDepartment.objects.all()
    return department
