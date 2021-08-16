## Running Tests on Project

***

* Following are the steps to run unit tests on the python project - ***Analytics on UN Population***

## Installation and Testing

***

* These are some basic steps to follow for installation of the project

* Create a folder in your local machine and run the following command in the terminal set the path to that directory

```bash
 git init
```

* Now click on the clone button on the repository page of the project(link: <>)
* Now click on clone via HTTPS option , an address will be copied to your clipboard
* Now run the following command in your machine's terminal and paste the address

```bash
 git clone <paste the address here>
```

* All the project files and folders will be cloned to your local system inside the folder
* Through terminal you have to install all the software requirements of the project which has been specifies in the requirements.txt file.
Run the following command to install all the library and packages.

```bash
 pip3 install -r requirements.txt
```

* Next you can run tests on the project main file that is main.py via running this command

```bash
 python3 -m unittest test_main.py
```

* In the terminal it will show something like

```bash
---------------------------------
Ran 4 tests in 0.001s

OK
```

* This means all the tests are instantiated with all the files and no error occured