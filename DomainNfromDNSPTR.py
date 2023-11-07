"""Write a function that takes an IP address and returns the domain name using PTR DNS records.
Example

get_domain("8.8.8.8") ➞ "dns.google"

get_domain("8.8.4.4") ➞ "dns.google"""

import socket

def get_domain(ip_address):
    ipAddress = socket.gethostbyaddr(ip_address)
    return ipAddress

print(get_domain("8.8.8.8"))

