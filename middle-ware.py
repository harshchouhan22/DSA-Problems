#Middleware to Redirect Non-WWW Requests to WWW:

class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.get_host().startswith('www.'):
            url = request.build_absolute_uri(request.get_full_path())
            url = url.replace('//', '//www.', 1)
            return HttpResponsePermanentRedirect(url)
        return self.get_response(request)
    





