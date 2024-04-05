import hashlib
from rest_framework.views import APIView
from rest_framework.response import Response
import socket
import random
from rest_framework.renderers import JSONRenderer


class HashView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        hostname = socket.gethostname()
        server_ip = socket.gethostbyname(hostname)
        ip_hash = str(server_ip)
        random_hash = str(random.random())

        # 500,000번 반복
        for _ in range(250_000):
            ip_hash = hashlib.sha256(ip_hash.encode()).hexdigest()
            random_hash = hashlib.sha256(random_hash.encode()).hexdigest()

        return Response(
            {
                "random_hash": random_hash,
                "ip_hash": ip_hash,
            }
        )
