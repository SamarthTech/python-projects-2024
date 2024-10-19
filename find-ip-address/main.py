# Import the necessary module!
import socket as s 

# Get my hostname
my_hostname = s.gethostname()
# Display my hostname
print("Your Hostname is: " + my_hostname)

# Get my IP
my_ip = s.gethostbyname(my_hostname)
# Display my IP 
print("Your IP Address is: " + my_ip)

# Set the hostname
host = "github.com"
# Fetch the IP
ip = s.gethostbyname(host)

# Display the IP
print("The IP Address of " + host + " is: " + ip)