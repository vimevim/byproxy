# ByProxy

ByProxy is a library to generate proxy dictionaries from a list of urls.

- It has two main classes:
  - ProxyChecker:
    - It requires Session object to make requests.
    - It helps us to gain information about our proxies.
    - check_my_ip is a method which basically sends a requests to the httpbin.org/ip and returns a dictionary.
    - target_ip_details is a method that sends requests to demo.ip-api.com to check the details of the target ip.
      - Be carefull when using this method, I aim no harm to the ip-api's servers. It's just a helper method for me to find out the details of the target ip. If you are going to use this method frequently, please consider purchasing a subscription from ip-api. I am not responsible for any damage caused by using this method.
    - check_target_url is a method that sends a get request to the target url to check if the proxy is working with the target url.
  - ProxyMaker:
    - It doesn't require any arguments.
    - It helps us to prepare the proxy dictionary.
- Todos:
  - [x] Implement a ProxyChecker class to check the proxies.
    - [x] Implement a check_my_ip method to verify the ip of the proxy.
    - [x] Implement a check_target_url method to verify if the proxy is working with the target url.
    - [x] Implement a target_ip_details method to get more information about the target ip.
  - [x] Implement a ProxyMaker class to prepare the proxy dictionary.
    - [x] Implement a read_lines method to read the lines from a file with given path and returns a list.
    - [x] Implement a split_lines method to split the lines from the list. It takes two arguments, lines and separator. It returns a list of lists.
    - [x] Implement a lines_to_dict method to convert the list of lists to a dictionary. It takes two arguments, lines and keys.
    - [x] Implement a make_proxies method to make the proxy dictionary. It takes three arguments, lines, type and password_enabled. It returns a dictionary of proxies which you can use with requests.Session object.
