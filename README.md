# Rasa Chatbot

## React Front-end
[https://github.com/BrunoInacio/chat-front-end/](https://github.com/BrunoInacio/chat-front-end/ "React Front-end")
 
## Virtual Environment 

### Create virtual environment
#### Linux
```sh
python3 -m venv <dir name>
````
#### Windows
```sh
python -m venv <dir name>
````

### Activate virtual environment
```sh
<dir name>/Scripts/Activate.ps1 
````

### Dectivate virtual environment
```sh
deactivate
````

## Packages
All packages can be installed in the virtual environment running the command:
```
pip install rasa 
```
Just make sure you have a 64-bit version of Python 3.7, required by some of the libraries (e.g. TensorFlow).

## Run Servers
Both servers must be running to use the bot.

### Main server
```
rasa run 
```

### Custom actions server
```
rasa run actions
```
