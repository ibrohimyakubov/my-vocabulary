from app.models import BigDepartment
from user.models import CustomUser


def departments(request):
    user = CustomUser.objects.get(username=request.user.username)
    department = BigDepartment.objects.filter(user=user)[:4]
    return {'department': department, 'user': user}
