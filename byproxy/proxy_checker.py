from requests import Session

class ProxyChecker:
    """
    ProxyChecker is a class that contains methods for checking proxies.     
    """
    def __init__(self, session: Session):
        self.session = session
    
    def target_ip_details(self, host, fields):
        """
        Get details about an IP address.
        
        Get details about an IP address from the ip-api.com API.
        
        Args:
            host (str): The IP address to get details about.
            fields (str): The fields to return. See the ip-api.com API for more details.
        
        Returns:
            dict: A dictionary containing the details about the IP address.
        """
        old_headers = self.session.headers.copy()
        self.session.headers["Origin"] = 'https://ip-api.com'
        url = f"https://demo.ip-api.com/json/{host}?fields={fields}&lang=en"
        response = self.session.request("GET", url)
        self.session.headers = old_headers
        return response
    
    def check_my_ip(self):
        """
        Check the IP address of the proxy.
        """
        url ="http://httpbin.org/ip"
        response = self.session.get(url)
        return response

    def check_target_url(self, url, timeout = 5):
        """
        Check the target URL.
        
        Args:
            url (str): The URL to check.
            timeout (int): The timeout in seconds. Defaults to 5.
        
        Returns:
            dict: A dictionary containing the status code and the response time.
        """
        response = self.session.get(url, timeout = timeout)
        return response