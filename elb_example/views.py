import hashlib
from rest_framework.views import APIView
from rest_framework.response import Response
import random


class HashView(APIView):
    def get(self, request):
        # 초기 해시 값
        initial_hash = str(random.getrandbits(256))

        # 1,000,000번 반복
        for _ in range(1_000_000):
            initial_hash = hashlib.sha256(initial_hash.encode()).hexdigest()

        return Response({"hash": initial_hash})
