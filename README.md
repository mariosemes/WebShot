<p align="left">
  <img width="180" height="180" src="https://github.com/mariosemes/WebShot/blob/master/images/logo.png?raw=true">
</p>

# WebShot - Make your life easier.

[![GitHub Release](https://github-basic-badges.herokuapp.com/release/mariosemes/WebShot.svg)]() [![GitHub Download Count](https://github-basic-badges.herokuapp.com/downloads/mariosemes/WebShot/total.svg)]() [![GitHub Issues Open](https://github-basic-badges.herokuapp.com/issues/mariosemes/WebShot.svg)]()

Website Screenshot Tool for Frontend Developers & Web Designers.
The tool creates screenshots of the website you are working on in defined resolutions.
Download and test it yourself!

![optimisation](https://github.com/mariosemes/WebShot/blob/master/images/preview.png?raw=true)

## How to use
1. Run the Tool
2. Select one of the given options
3. When asked, paste or write the URL you want to check
4. The tool will create a folder on your desktop based on the domain name
5. At the end, the tool will open up the folder where the WebShots are


## Changing Resolutions.ini
If its your first time running the tool, it will create a resolutions.ini file that holds the testing resolutions.
You can add, edit, remove any resolution you want and even create custom blocks too.

**Example:**
```sh
[MyTestingResolutions]
ThisIsMyTestingResolution = 1024x1024
```

## Using the LOGIN option
If your website user needs to be logged in to see the website, that's when you need the LOGIN option.
Run the tool and select "Create new login.ini" and type whatever name you want it to be, like (wordpress).
The tool will create a file name wordpress.ini and open it up so it will look like this:

```sh
[login]
login_url = 
user_x_path = 
username = 
pass_x_path = 
password = 
login_button = 
```
Let me explain every single one of them:
```sh
login_url = https://yourdomain.com/wp-admin (selfexplainable but something like this)
user_x_path = /html/body/div[2]/div[2]/div[1]/ (XPath of the username input field)
username = your_user_name (your username)
pass_x_path = /html/body/div[2]/div[3]/div[2]/ (XPath of the password input field)
password = your_password (your password)
login_button = /html/body/div[2]/div[3]/div[2]/ (XPath of the login button field)
```
So, a good example of a login.ini file would look like this:
```sh
login_url = https://yourdomain.com/wp-admin
user_x_path = /html/body/div[2]/div[2]/div[1]/
username = thisismynickname
pass_x_path = /html/body/div[2]/div[3]/div[2]/
password = your_password
login_button = /html/body/div[2]/div[3]/div[2]/
```
Thats it.
When you are done with editing the create "wordpress.ini" login file, select an option on the tool that ends with "with login" as "WebShot Single Url with Login" and the tool will ask you to select one of the created .ini files.

## Download for Windows/Linux - [Releases page](https://github.com/mariosemes/WebShot/releases/)
Mac - Work in progress


## Installation
[Linux](#linux) | [Windows](#windows) | Mac (Work in progress)

#### Linux
1. Open terminal and install Chromium if you don't have it:
```sh
$ sudo apt install chromium
```
2. Install ChromeDriver if you don't have that too:
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
4. WebShot will create a resolutions.ini file where you can chande, add or remove resolutions
5. WebShot will try to download the latest chromedriver.exe from the official website

## Troubleshooting
#### Windows
If you encounter any problems, please try to delete the "chromedriver.exe" inside the root folder of WebShot.exe and try to run it again.
ChromeDriver.exe runs and talks to your chrome.exe browser. In case the versions are different, chromedriver.exe will sometimes make problems.
In this case, if you delete the chromedriver.exe and let WebShot redownload it again, this should fix most of the problems.

#### Linux
In case you are having problems, please open Terminal and type:
```sh
$ chromium --version
$ chromedriver --version
```
Check if the versions are the same. In case they are not, please apt update them.


## Todos

 - Create ERROR logging
 - ~~First run checker~~
 - Create custom resolution validator

License
----

Licence GNU GPLv3