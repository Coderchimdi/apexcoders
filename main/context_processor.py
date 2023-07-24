from .models import AppInfo, Category

def apex(request):
  info = AppInfo.objects.get(pk=1)
  category = Category.objects.all()
  context = {
    'info': info,
    'category': category,
  }

  return context