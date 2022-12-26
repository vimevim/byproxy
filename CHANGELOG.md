# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Version 0.1.2.2 - 2022-12-26

### Added

* Added another function to "ProxyMaker" class. It's called "make_proxy" and it requires a single dict with keys "host", "port", "username" and "password". It returns a single proxy dict.

### Fixed

* "make_proxies" function in "ProxyMaker" class. It had a problem, it requires a list of dict with keys "host", "port", "username" and "password" but used index instead of key.

### Internal

* "make_proxies" function now uses "make_proxy" function to make proxies.

## Version 0.1.2.1 - 2022-12-25

### Fixed

* Dependency conflicts.

## Version 0.1.2 - 2022-12-14

### Added

* CHANGELOG.md file
* README.md file
* Git repository

### Fixed

* Nothing yet...

### Internal

* Nothing yet...

### Removed

* Nothing yet...

### Changed

* Nothing yet...
