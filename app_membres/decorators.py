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
        membre_id = request.session.get("client", {}).get("id")
        from app_membres.models import Profil
        profil_exists = Profil.objects.filter(membre_id=membre_id).exists() if membre_id else False
        referer = request.META.get('HTTP_REFERER', '')
        # Ne pas rediriger si déjà sur la page membres
        if request.path == '/membres/':
            return view_func(request, *args, **kwargs)
        if 'membres' in referer:
            return redirect('membres')
        if not membre_id or not profil_exists:
            return redirect('membres')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def attente_validation_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        membre_id = request.session.get("client", {}).get("id")
        from app_membres.models import Profil
        profil = Profil.objects.filter(membre_id=membre_id).first()
        # Si l'utilisateur est connecté et déjà sur la page membres, il ne doit pas accéder à attente_validation
        if membre_id and request.path == '/attente_validation/':
            return redirect('membres')
        if not membre_id or (profil and not getattr(profil, 'valider', False)):
            return redirect('membres')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

