# Chroma DB Experiments

Environment: WSL2 for Windows 11 with Ubuntu 22.04 and Python 3.10.x with venv

Editor: VS Code with WSL, Python, and Pylance extensions 

The Python virtual environment was configured as follows:

```
~> python3 --version # Should be 3.10.x (Chroma doesn't yet support 3.11 due to pytorch.)
~> sudo apt install python3-venv # Install venv to manage virtual environments
~> mkdir python-project && cd python-project # New folder for a python project
~> python3 -m venv .venv # Create a virtual environment called .venv
~> source .venv/bin/active # Active the virtual environment
~> pip install chromadb # Install chroma db.
~> pip install black # For VS Code source formatting.
```
