# ByProxy

ByProxy is a simple package contains simple tools for proxy management and usage. You can generate proxy dictionaries from a list of urls and gain information about the proxies.

Check out the [byproxy API documentation](https://vimevim.github.io/byproxy/) for more information.

## Todos

- [x] Implement a ProxyChecker class to get information about the proxies.
  - [x] Implement a check_my_ip method to verify the ip of the proxy.
  - [x] Implement a check_target_url method to verify if the proxy is working with the target url.
  - [x] Implement a target_ip_details method to get more information about the target ip.
  - [x] Implement an async_api method to make async requests.
- [x] Implement a ProxyMaker class to prepare the proxy dictionary.
  - [x] Implement a read_lines method to read the lines from a file with given path and returns a list.
  - [x] Implement a split_lines method to split the lines from the list. It takes two arguments, lines and separator. It returns a list of lists.
  - [x] Implement a lines_to_dict method to convert the list of lists to a dictionary. It takes two arguments, lines and keys.
  - [x] Implement a make_proxies method to make the proxy dictionary. It takes three arguments, lines, type and password_enabled. It returns a dictionary of proxies which you can use with requests.Session object.
- [ ] Find a way to validate the proxy format and implement a method to validate proxies.
- [ ] Improve documentation, changelog, dependencies and readme.
- [ ] Add examples.
