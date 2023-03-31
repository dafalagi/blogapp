from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'admin/index.html')

def components(request, title):
    if title == 'alerts':
        return render(request, 'admin/components/components-alerts.html')
    elif title == 'accordion':
        return render(request, 'admin/components/components-accordion.html')
    elif title == 'badges':
        return render(request, 'admin/components/components-badges.html')
    elif title == 'breadcrumbs':
        return render(request, 'admin/components/components-breadcrumbs.html')
    elif title == 'buttons':
        return render(request, 'admin/components/components-buttons.html')
    elif title == 'cards':
        return render(request, 'admin/components/components-cards.html')
    elif title == 'carousel':
        return render(request, 'admin/components/components-carousel.html')
    elif title == 'list-group':
        return render(request, 'admin/components/components-list-group.html')
    elif title == 'modal':
        return render(request, 'admin/components/components-modal.html')
    elif title == 'tabs':
        return render(request, 'admin/components/components-tabs.html')
    elif title == 'pagination':
        return render(request, 'admin/components/components-pagination.html')
    elif title == 'progress':
        return render(request, 'admin/components/components-progress.html')
    elif title == 'spinners':
        return render(request, 'admin/components/components-spinners.html')
    elif title == 'tooltips':
        return render(request, 'admin/components/components-tooltips.html')

def data_tables(request):
    return render(request, 'admin/tables/tables-data.html')

def forms(request, title):
    if title == 'elements':
        return render(request, 'admin/forms/forms-elements.html')
    elif title == 'layouts':
        return render(request, 'admin/forms/forms-layouts.html')
    elif title == 'editors':
        return render(request, 'admin/forms/forms-editors.html')
    elif title == 'validation':
        return render(request, 'admin/forms/forms-validation.html')

def icons(request, title):
    if title == 'bootstrap':
        return render(request, 'admin/icons/icons-bootstrap.html')
    elif title == 'remix':
        return render(request, 'admin/icons/icons-remix.html')
    elif title == 'boxicons':
        return render(request, 'admin/icons/icons-boxicons.html')

def profile(request):
    return render(request, 'admin/users-profile.html')

def faq(request):
    return render(request, 'admin/pages/pages-faq.html')

def contact(request):
    return render(request, 'admin/pages/pages-contact.html')

def register(request):
    return render(request, 'admin/pages/pages-register.html')

def login(request):
    return render(request, 'admin/pages/pages-login.html')

def error(request):
    return render(request, 'admin/pages/pages-error-404.html')

def blank(request):
    return render(request, 'admin/pages/pages-blank.html')