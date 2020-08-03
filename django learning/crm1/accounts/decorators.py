from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_users(view_functions):
    def wrapperfunctions(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_functions(request, *args, **kwargs)
    return wrapperfunctions

def user_allowed(allowed_user=[]):
    def decorators(view_functions):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_user:
                view_functions(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed to view this page ')

            return view_functions(request, *args, **kwargs)
        return wrapper_func
    return decorators
