class ProxyMaker:
    def read_lines(self, path):
        """
        Read lines from a file.
        
        Args:
            path (str): Path to the file.
        Returns:
            list: List of lines.
        """
        with open(path, 'r') as f:
            return f.read().splitlines()
    
    def split_lines(self, lines, separator = ":"):
        """
        Split lines into a list of lists.
        
        Args:
            lines (list): List of lines.
            separator (str): Separator to split the lines. Defaults to ":".
        Returns:
            list: List of lists.
        """
        return [line.split(separator) for line in lines]    
    
    def lines_to_dict(self, lines, keys = ["host", "port", "username", "password"]):
        """
        Convert a list of lists to a list of dictionaries.
        
        Args:
            lines (list): List of lists.
            keys (list): List of keys in order. Defaults to ["host", "port", "username", "password"].
        Returns:
            list: List of dictionaries.
        """
        return [dict(zip(keys, l)) for l in lines]
    
    def make_proxies(self, proxy_dicts, type, password_enabled = False):
        """
        Make proxies from a list of dictionaries.
        
        Args:
            proxy_dicts (list): List of dictionaries with keys "host", "port", "username", "password".
            type (str): Type of proxy, http or https.
            password_enabled (bool): Whether the proxy requires a password. Defaults to False.
        
        Returns:
            list: List of proxies.
        """
        proxies = []
        for proxy_dict in proxy_dicts:
            proxies.append(self.make_proxy(proxy_dict, type, password_enabled))
        return proxies
    
    def make_proxy(self, proxy_dict, type, password_enabled = False):
        """
        Make proxies from a list of dictionaries.
        
        Args:
            proxy_dict (dict): A dict with keys "host", "port", "username", "password".
            type (str): Type of proxy, http or https.
            password_enabled (bool): Whether the proxy requires a password. Defaults to False.
        
        Returns:
            list: List of proxies.
        """
        if password_enabled:
            proxy = { # United States - Does not work
                "http": f"{type}://{proxy_dict['host']}:{proxy_dict['port']}@{proxy_dict['username']}:{proxy_dict['password']}/",
                "https": f"{type}://{proxy_dict['host']}:{proxy_dict['port']}@{proxy_dict['username']}:{proxy_dict['password']}/",
            }
        else:
            proxy = { # United States - Does not work
                "http": f"{type}://{proxy_dict['host']}:{proxy_dict['port']}/",
                "https": f"{type}://{proxy_dict['host']}:{proxy_dict['port']}/",
            }
        return proxy