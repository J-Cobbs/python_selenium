# Table of content

- [Python + Selenium + PyCharm](#python--selenium--pycharm)
- [What is this for?](#what-is-this-for)
- [Improvement](#improvement)
- [Bonus - Allure Report](#bonus---allure-report)


# Python + Selenium + PyCharm

This project was created for the automation practice using the Python and Selenium in PyCharm IDE.

# What is this for?

I'm always trying to grow and learn something new. Just like with JS repository, here I'm improving my automation skills with Python.

# Improvement

I know, these tests has spaghetti code, and will need some proper page object pattern. Once I will have some more time I will try to add it also, so the code will looks much better.

# Bonus - Allure Report

It' won't be in my project, hovewer I have checked it whether it works. Because these steps worked in my project I will show how to bring Allure to the project.

## Allure library download for raport generation
1. Under http://allure.qatools.ru/ website, we will find official Allure software
2. In the upper right corner there is a Download link which will redirect us to the resource with the latest version of the Allure software available for download on the GitHub platform (currently the latest version is 2.13.8)
3. Unpack the file and copy the entire contents.
4. Create a libs directory in our project (in PyCharm, in the Projects view, right-click the context menu and use the New-> Directory option).
5. Paste the file (not via PyCharm) to the newly created folder

### Installing packages via PIP
1. Open the terminal
2. Enter the folder of our project
3. PIP is a Python package manager. To use it, just open the console (maybe the one with PyCharm) and type: `pip3` (for macOS)
4. After its execution, we will get a list of help topics and sample parameters
5. The most commonly used commands are:
- pip3 list - displays information about all installed packages and their versions,
- pip3 install xxx - installs package named xxx,
- pip3 uninstall xxx - Removes package named xxx.

### Installation of the Allure package
We have already installed the library for generating Allure reports, but we still need a proper library to prepare the test results so that the generator "consumes" them correctly.

In our case, you will need the Allure package for Python.
For this we need to know the exact name of the package. We can find out at https://pypi.org/, where there is a list of available packages.

After entering Allure, you will see a list of available packages, and in the first position - Allure-Pytest (currently: 2.8.34). After visiting the link https://pypi.org/project/allure-pytest/ we will get information about the package, documentation and how to install it.

So we install the allure package: `pip3 install allure-Pytest` or `brew install allure`

## Running tests
1. Make sure you have some tests written already
2. You are in the folder where the file You run is located - generally in the design folder - run: 
`python3 -m Pytest <folder_name_if_exists>/<test-name> .py --alluredir ./results`
3. If the file is in another folder, e.g. test_suites, then the folder must be placed in the code

Let's add `if __name__ == '__main__':` before initializing the `runner` so that the tests don't run twice. With this minor change, if pytest is given **testsuite_example.py** to run tests, only the imported classes will be called, `runner.run ()` not. In addition, this small change will keep the unittest compatible, so you can still use **TestSuite** as before,

4. Run the test suite (in my case the code looks like this:
`python3 -m Pytest test_suites/testsuite_example.py --alluredir ./results`
5. After starting it, we should see the result in the console
6. The results after our tests will be in the results folder - there are a lot of files with random names, with the `.json` extension - these are the results of the "raw" version of the test.
At the moment this is not very readable, but now you can use the Allure library (which was downloaded at the beginning and placed in the libs directory) to generate a nice report based on the results of our tests

## Generating a report
1. Open a PyCharm terminal - you should be in your project folder
2. Run the command (macOS): `allure serve ./results/` → this one worked for me or `libs / allure-2.13.7 / bin / allure serve ./results`
- It runs the **allure** file, which is located in libs \ allure-2.6.0 \ bin \ allure.
- It uses the **serve** command which is responsible for generating the report.
- It shows us where the files with test results for the report are, i.e. `./results`.
3. We should see a report running, the results of which can be downloaded in * .csv
4. You can terminate the server with `ctrl + c`
