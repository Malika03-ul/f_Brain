from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import IPTranslation
import ipaddress

@api_view(['POST'])
def translate_ipv4_to_ipv6(request):
    try:
        ipv4 = request.data.get('ipv4')
        if not ipv4 or not ipaddress.ip_address(ipv4).version == 4:
            return Response({'error': 'Invalid IPv4 address'}, status=status.HTTP_400_BAD_REQUEST)

        # Simple IPv4-mapped IPv6 conversion
        ipv6 = f"::ffff:{ipv4}"
        # Store the conversion in the database
        translation = IPTranslation.objects.create(ipv4=ipv4, ipv6=ipv6)
        return Response({'ipv6': ipv6}, status=status.HTTP_200_OK)
    except ValueError:
        return Response({'error': 'Invalid IP address format'}, status=status.HTTP_400_BAD_REQUEST)