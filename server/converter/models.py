from django.db import models

class Conversion(models.Model):
    ipv4 = models.GenericIPAddressField(protocol='IPv4')
    ipv6 = models.GenericIPAddressField(protocol='IPv6')
    created_at = models.DateTimeField(auto_now_add=True)