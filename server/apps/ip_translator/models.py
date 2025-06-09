from django.db import models

class IPTranslation(models.Model):
    ipv4 = models.GenericIPAddressField(protocol='IPv4')
    ipv6 = models.GenericIPAddressField(protocol='IPv6')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ipv4} -> {self.ipv6}"