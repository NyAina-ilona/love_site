from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def membre_validation_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'member'):
            if not request.user.member.validation:  
                return redirect('activer_compte')  
        return view_func(request, *args, **kwargs)
    return wrapper

def condition_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        client = request.session.get("client")
        membre_id = client.get("id") if client else None
        if membre_id:
            from app_membres.models import Profil
            profil_exists = Profil.objects.filter(membre_id=membre_id).exists()
            if not profil_exists and request.path != '/condition_admi/':
                return redirect('condition_admi')
        elif request.path == '/login/' or request.path == '/register/' or request.path == '/aff_login/' or request.path == '/aff_register/':
            # Allow access to login and register pages even if not logged in
            return view_func(request, *args, **kwargs)
        else:
            # If no membre_id, redirect to the correct login view
            return redirect('aff_login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
