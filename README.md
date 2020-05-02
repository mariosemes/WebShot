<p align="left">
  <img width="180" height="180" src="https://github.com/mariosemes/WebShot/blob/master/images/logo.png?raw=true">
</p>

## WebShot Desktop Tool

[![GitHub Release](https://github-basic-badges.herokuapp.com/release/mariosemes/WebShot.svg)]() [![GitHub Download Count](https://github-basic-badges.herokuapp.com/downloads/mariosemes/WebShot/total.svg)]() [![GitHub Issues Open](https://github-basic-badges.herokuapp.com/issues/mariosemes/WebShot.svg)]()

Website Screenshot Tool for Frontend Developers & Web Designers.
The tool creates screenshots of the website you are working on in defined resolutions.
Download and test it yourself!

![optimisation](https://github.com/mariosemes/WebShot/blob/master/images/preview.png?raw=true)

## How to use
1. Run the Tool
2. When asked, paste or write the URL you want to check
3. The tool will create a folder on your desktop named based on the domain
4. All images can be found there and the tool will close itself when its done


## Changing Settings.ini
If its your first time running the tool, it will create a Settings.ini file that holds the testing resolutions.
You can add, edit, remove any resolution you want and even create custom blocks too.

**Example:**
```sh
[MyTestingResolutions]
ThisIsMyTestingResolution = 1024x1024
```

## Download for Windows/Linux - [Releases page](https://github.com/mariosemes/WebShot/releases/)
Mac - Work in progress


## Installation
[Linux](#linux)
[Windows](#windows)
Mac (Work in progress)

#### Linux
1. Open terminal and install Chromium if you dont have it:
```sh
$ sudo apt install chromium
```
2. Install Chromedriver if you dont have that too:
```sh
$ sudo apt install chromium-chromedriver
```
3. Download WebShot script from the Releases page.
4. Unzip it and put it whereever you want.
5. Apply permission to execute:
```sh
$ chmod +x /path/to/webshot
```
6. Optional: if you want to use the script globally, then you need to copy the file to your /usr/local/bin directory, is better if you copy it without the .sh extension:
```sh
$ sudo cp /path/to/webshot /usr/local/bin/webshot
```
7. Open terminal window and type: "webshot"

#### Windows

1. Download the tool from the Releases page
2. Unzip it and place it whereever you want
3. Run WebShot.exe


## Todos

 - Create ERROR logging
 - First run checker

License
----

Licence GNU GPLv3