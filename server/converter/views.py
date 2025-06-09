from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import ipaddress
from .models import Conversion

@api_view(['POST'])
def convert_ip(request):
    ipv4_str = request.data.get('ipv4')
    try:
        ipv4 = ipaddress.IPv4Address(ipv4_str)
        ipv6 = ipaddress.IPv6Address('::ffff:' + str(ipv4))
        conversion = Conversion(ipv4=str(ipv4), ipv6=str(ipv6))
        conversion.save()
        return Response({'ipv6': str(ipv6)}, status=status.HTTP_200_OK)
    except ipaddress.AddressValueError:
        return Response({'error': 'Adresse IPv4 invalide'}, status=status.HTTP_400_BAD_REQUEST)