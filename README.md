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
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
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

:warning: If you see a message like this in the log, remove the comments from launch.json:
```
  File "/Users/roelfie/workspace/vscode/learning-python/.vscode/launch.json", line 2
    // Use IntelliSense to learn about possible attributes.
    ^
SyntaxError: invalid syntax
```

## Characteristics of the python language

* dynamically typed
* strongly typed
* single-line comment `# some comment`
* multi-line comments (like `/* bladibla ... */` in Java) not supported 


