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
    
    def make_proxies(self, lines, type, password_enabled = False):
        """
        Make proxies from a list of dictionaries.
        
        Args:
            lines (list): List of dictionaries.
            type (str): Type of proxy.
            password_enabled (bool): Whether the proxy requires a password. Defaults to False.
        
        Returns:
            list: List of proxies.
        """
        proxies = []
        if password_enabled:
            for line in lines:
                proxy = { # United States - Does not work
                    "http": f"{type}://{line[2]}:{line[3]}@{line[0]}:{line[1]}/",
                    "https": f"{type}://{line[2]}:{line[3]}@{line[0]}:{line[1]}/",
                }
                proxies.append(proxy)
        else:
            for line in lines:
                proxy = { # United States - Does not work
                    "http": f"{type}://{line[0]}:{line[1]}/",
                    "https": f"{type}://{line[0]}:{line[1]}/",
                }
                proxies.append(proxy)
        return proxies