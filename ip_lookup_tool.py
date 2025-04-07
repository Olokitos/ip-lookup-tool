
import ipaddress
import requests
import logging

# Set up logging
logging.basicConfig(
    filename='ip_lookup.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to validate IP address
def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Function to get IP info from API
def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        if response.status_code == 200:
            data = response.json()
            return {
                "IP": data.get("ip", "N/A"),
                "City": data.get("city", "N/A"),
                "Region": data.get("region", "N/A"),
                "Country": data.get("country", "N/A"),
                "Org": data.get("org", "N/A"),
                "Location": data.get("loc", "N/A")
            }
        else:
            return {"Error": "API Error"}
    except Exception as e:
        logging.error("API request failed", exc_info=True)
        return {"Error": str(e)}

# Main program loop
def main():
    ip = input("Enter an IP address (IPv4 or IPv6): ")
    
    if is_valid_ip(ip):
        logging.info(f"User entered valid IP: {ip}")
        info = get_ip_info(ip)
        print("\n--- IP Information ---")
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        logging.warning(f"User entered invalid IP: {ip}")
        print("Invalid IP address.")

if __name__ == "__main__":
    main()
