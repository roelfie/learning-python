# Learning Python

Playground for the course Learning Python by Joe Marini on LinkedIn Learning

## Preparations

```
$ python --version
Python 2.7.16

$ python3 --version
Python 3.7.6 
```

Run `/Applications/Python 3.8/Install Certificates.command` to install TLS root certificates.

### vscode
You can change the Python version used by the Python extension in vscode
* in the bottom toolbar of vscode
* in 'python version' under Extensions/Python in the vscode settings (e.g. 'python' for Python v2 and 'python3' for Python v3)

## Hello World

Python is an interpreted language (like JavaScript). You don't have to compile the source code and build an executable before you can run it (like Java or C/C++).

#### from the command line
`$ python3 helloWorld.py` 

#### from the python shell
```
$ python3
Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) (...)
>>> 2+2
4
>>> print("Hello world!")
Hello world!
>>> exit()
$ 
```

#### with the vscode debugger
When you open the debug view in vscode for the first time, there are no launch configurations. Click the "create a launch.json file" link and choose "Python file (debug the currently active Python file)". A file `.vscode/launch.json` will be created:
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```
Now open a `*.py` file in vscode and in the debug view, hit the "Start debugging" button (green triangle).

## Characteristics of the Python language

* dynamically typed
* strongly typed
* single-line comment `# some comment`
* multi-line comment (like `/* bladibla ... */` in Java) not supported 
* scope defined by colon & indentation (instead of curly braces in Java)
* no equivalent of the Java switch statement (use `if` / `elif` / `else` instead)
* for-loops:
  * `while(condition):`
  * `for x in range(5, 10):`
  * `for x in <collection>:`
  * `for i,x in enumerate(<collection>):` gives you access to the loop counter

## Documentation

* [python 3.8 documentation](https://docs.python.org/3.8/index.html)
  * [datetime](https://docs.python.org/3.8/library/datetime.html)
  * [timedelta](https://docs.python.org/3.8/library/datetime.html#timedelta-objects)
    * `print ("one week from now it will be: " + str(datetime.now() + timedelta(weeks=1)))`
    * supports seconds, minutes, hours, days and weeks; but not months or years!
  * [calendar](https://docs.python.org/3.8/library/calendar.html)
    * generate a (highly configurable) HTML calendar for a specific month
    * iterate over the weekdays, monthdays, monthdates, yeardays, yeardates, ..
    * calculate the first wednesday of each month, etc. etc.
  * [files](https://docs.python.org/3.8/library/filesys.html) basic file operations like reading and writing are available by default (no import needed)
  * [os](https://docs.python.org/3.8/library/os.html) information about the OS, environment, path utilities, file descriptors, etc.
  * [shutil](https://docs.python.org/3.8/library/shutil.html) shell utilities like copy, rename, archive (zip/tar/..)
  * [zipfile](https://docs.python.org/3/library/zipfile.html) fine grained control over zip file creation

#### datetime formatting

* [datetime.strftime("The current date is %x")](https://docs.python.org/3.8/library/datetime.html#strftime-strptime-behavior)
  * `%y`: year
  * `%b`: month
  * `%d`: day
  * `%a`: weekday
  * `%c`: local date time
  * `%x`: local date
  * `%X`: local time
  * `%H`: hours (24)
  * `%I`: hours (12)
  * `%M`: minutes
  * `%S`: seconds 
  * `%p`: AM/PM

