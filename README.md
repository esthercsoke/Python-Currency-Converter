

# Currency Converter in Python

![Terminal](https://badgen.net/badge/icon/terminal?icon=terminal&label)
## Author
<b>Name:</b> Esther Csoke
<b>Student ID:</b> 24542312

--- 

## Description
<What your application does>

This python terminal application uses the [Frankfurter](https://www.frankfurter.app/) API to retrieve the current conversion rates between the inputs of 2 currency codes of a certain date using a date input. It returns the conversion and and an inverse conversion rate between the two currencies.


<Which Python version you used>

:snake: <b>Python:</b> 
Version: 3.8.9


<Which packages and version you used>

:package: <b>Packages used:</b>
- requests 2.28.1

Check out the requests documentation [here](https://pypi.org/project/requests/)


<Some of the challenges you faced>
<b>Challenges </b>

- Initially understanding the code structure. 
- Have worked in React JS for so long. I found difficult at first adapting to Python.
- Unit Testing, as I have only worked using strenuous and time consuming manual testing :muscle:

<b> Future Implementation:</b>

- Add fun terminal input to create a user interface in the terminal.
- Ability to download results to CSV.
- Add another argument for custom currency amount.


## How to Setup
<Provide a step-by-step description of how to get the development environment set and running.>

- Make sure you have Python on your computer. [Check here for installing Python](https://www.python.org/downloads/)
- Install the needed packages using `pip install <package>==<version number>`. Check the [PIP](https://pypi.org/project/pip/) documentaton for more information. 


## How to Run the Program
<Provide instructions and examples>

1. Download directory folder.
   <br>
2. In your terminal use `cd` to move into the folder directory.

In the terminal use the basic code structure of



```python
python main.py <date> <currency origin> <currency destination>
```



For example:

<center>


```python

$ python main.py 2021-07-16 GBP AUD
```

</center>
<br>
<b>The argument values in the terminal app have some rules:</b>

`date` Must have the format of `Y-m-d` (<i>e.g '2020-01-01'</i>)

`currency` Must be one of the valid currency abbreviations.
<br>


---

## Project Structure
<List all folders and files of this project and provide quick description for each of them>

<b>Overview</b>

 📦DSP_AT1_24542312
 ┣ 📜README.md
 ┣ 📜api.py
 ┣ 📜checks.py
 ┣ 📜currency.py
 ┣ 📜frankfurter.py
 ┣ 📜main.py 
 ┣ 📜test_api.py
 ┣ 📜test_checks.py
 ┣ 📜test_currency.py
 ┗ 📜test_frankfurter.py


| file      | Description |
| ----------- | ----------- |
| README.md    | The markdown file (this file) containing information on how to set up the python environment, what the project does and the instructions.     |
| api.py   |  The markdown file (this file) containing information on how to set up the python environment, what the project does and the instructions.       |
| checks.py   | file containing functions to check whether the currency and date inputs are valid.       |
| currency.py   | contains the class CurrencyConverter that contains methods to extract the currency conversion from the Frankfurter API and calculate the inverse rate.       |
| rfankfurter.py   | contains the class Frankfurter that contains methods responsible for calling relavant Frankfurther API endpoints.       |
| main.py   | contains the main functions from various other python files to execute the program       |
| test_api.py   | python script that will test the API GET request from  `api.py`        |
| test_checks.py   | Contains multile unittest functions to test the functions from `checks.py`        |
| test_currency.py   |The python script that will test the functions from the  CurrencyConverter class in `currency.py`        |
| test_frankfurter.py   | Contains the unittest functions to test the functions in `frankfurter.py` |

--- 


### The list of currencies available:</b>

 `AUD`: "Australian Dollar", `BGN`: "Bulgarian Lev", `BRL`: "Brazilian Real", `CAD`: "Canadian Dollar", `CHF`: "Swiss Franc", `CNY`: "Chinese Renminbi Yuan", `CZK`: "Czech Koruna", `DKK`: "Danish Krone",`EUR`: "Euro", `GBP`: "British Pound", `HKD`: "Hong Kong Dollar", `HRK`: "Croatian Kuna", `HUF`: "Hungarian Forint", `IDR`: "Indonesian Rupiah",`ILS`: "Israeli New Sheqel",`INR`: "Indian Rupee", `ISK`: "Icelandic Króna",`JPY`: "Japanese Yen",`KRW`: "South Korean Won",`MXN`: "Mexican Peso", `MYR`: "Malaysian Ringgit" `NOK`: "Norwegian Krone", `NZD`: "New Zealand Dollar", `PHP`: "Philippine Peso", `PLN`: "Polish Złoty",`RON`: "Romanian Leu", `SEK`: "Swedish Krona", `SGD`: "Singapore Dollar", `THB`: "Thai Baht", `TRY`: "Turkish Lira", `USD`: "United States Dollar", `ZAR`: "South African Rand"

 
## Citations
<Mention authors and provide links code you source externally>

- https://www.frankfurter.app/
- https://stackoverflow.com/questions/52181161/handling-exceptions-from-python-requests

- https://miguendes.me/3-ways-to-test-api-client-applications-in-python

- https://www.geeksforgeeks.org/python-unittest-assertalmostequal-function/