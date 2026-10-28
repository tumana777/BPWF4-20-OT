import time

class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        t1 = time.time()

        response = self.get_response(request)

        t2 = time.time()

        total_time = t2 - t1

        print(
            f"Method: {request.method}",
            f"Path: {request.path}",
            f"Status: {response.status_code}",
            f"User: {request.user}",
            f"IP: {request.META['REMOTE_ADDR']}",
            f"Time: {total_time:.4f} seconds"
        )

        return response


