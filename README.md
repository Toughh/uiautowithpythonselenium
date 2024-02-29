## Name
My Portal UI Automation Test Cases

## Description
This is the source of automated UI test cases for My Portal application

## Installation
1. Download and install below tool and software:

    - Python (Ver: 3.8)
    - Pycharm Editor

## Create a venv:
   - Go to File > Settings > Project: myportal_ui_automation > Python Interpreter
   - Click on settings icon to add interpreter
   - Browse Base Interpreter and Select Python/Python3.8/python.exe
   - Click on Apply and then Ok

## Install Requirements
   - Open requirements.txt 
   - Click on install requirement. Alternatively, `pip install -r requirements.txt`
   - Add additional command only for Linux OS: `sudo apt install  python3-tk python3-dev`

## Where to download drivers?
   - ChromeDriver (https://chromedriver.chromium.org/home)
   - GeckoDriver (https://github.com/mozilla/geckodriver/releases)
   - InternetExplorerDriver (https://www.selenium.dev/downloads/)
   - OperaDriver (https://github.com/operasoftware/operachromiumdriver/releases)

**Note**: InternetExplorerDriver is not supported with Linux

- ### Extract drivers in Windows OS
   - Download and extract drivers from above url
   - Put all extracted drivers under Python3.8/Scripts folder

- ### Extract drivers in Linux OS
   - Download and extract drivers from above url
     - Run the below command for ChromeDriver:
       * ```sudo mv chromedriver /usr/bin/chromedriver```
       * ```sudo chown root:root /usr/bin/chromedriver```
       * ```sudo chmod +x /usr/bin/chromedriver```
     - Run the below command for GeckoDriver:
       * ```sudo mv geckodriver /usr/bin/geckodriver```
       * ```sudo chown root:root /usr/bin/geckodriver```
       * ```sudo chmod +x /usr/bin/geckodriver```
     - Run the below command for EdgeDriver:
       * ```sudo mv msedgedriver /usr/bin/msedgedriver```
       * ```sudo chown root:root /usr/bin/msedgedriver```
       * ```sudo chmod +x /usr/bin/msedgedriver```
     - Run the below command for OperaDriver:
       * ```sudo mv operadriver /usr/bin/operadriver```
       * ```sudo chown root:root /usr/bin/operadriver```
       * ```sudo chmod +x /usr/bin/operadriver```

### Install allure for reporting purpose
    
    - For Linux:
        `curl -o allure-2.13.8.tgz -OLs https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz`
        `sudo tar -zxvf allure-2.13.8.tgz -C /opt/`
        `sudo ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure`
        `allure --version`
       
## Execution

- Create a directory **reports** under myportal_ui_automation

- ### From Windows OS
   
     ```pytest -v -s --alluredir="`Enter directory path where you want to save your report`" test```
   
      Ex: ```pytest -v -s --alluredir="C:\MyPortalUIAutomation\myportal_ui_automation\reports" "C:\MyPortalUIAutomation\myportal_ui_automation\test\client\dashboard\testDashboard.py"```

- ### From Linux OS
   
     ```pytest -v -s --alluredir="`Enter directory path where you want to save your report`" test```
   
      Ex: ```pytest -v -s --alluredir="/home/ubuntu/MyPortalUIAutomation/myportal_ui_automation/reports" /home/ubuntu/MyPortalUIAutomation/myportal_ui_automation/test/client/application/testProofOfAddress.py```

- ### Generate allure report:
 
     ```allure serve "Your report path"```

      Ex: ```allure serve C:\MyPortalUIAutomation\myportal_ui_automation\reports```
      Ex: ```allure serve /home/ubuntu/MyPortalUIAutomation/myportal_ui_automation/reports```

**Note**: Always delete the reports content except .gitkeep before a new run

## Additional Information

- To uninstall single requirement:
   - ```pip uninstall {your requirement}```
   
     Ex: ```pip uninstall jsonpath```