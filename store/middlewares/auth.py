
from django.shortcuts import redirect
from django.contrib import messages
def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request.session.get('customer'))
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'):
            messages.info(request,"Login first")
            return redirect('login')

        response = get_response(request)
        return response

    return middleware