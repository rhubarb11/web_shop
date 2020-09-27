from . models import Category, SubCategory



def get_categories(request):
    categories = Category.objects.all()

    for c in categories:
        c.sub_categories = SubCategory.objects.filter(category__name=c.name)

    context = {'categories': categories}
    return context;
