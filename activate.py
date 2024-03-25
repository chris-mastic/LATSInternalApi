import os
import sys

def deactivate():
    global deactivate  # Declare 'deactivate' as a global variable

    # Reset old environment variables
    if "_OLD_VIRTUAL_PATH" in globals():
        PATH = _OLD_VIRTUAL_PATH
        os.environ["PATH"] = PATH
        del _OLD_VIRTUAL_PATH

    # Unset virtual environment variables
    VIRTUAL_ENV = None
    VIRTUAL_ENV_PROMPT = None

  
# Unset irrelevant variables
deactivate()

VIRTUAL_ENV = "/var/www/LATSInternalApi/venv"
os.environ["VIRTUAL_ENV"] = VIRTUAL_ENV

_OLD_VIRTUAL_PATH = os.environ.get("PATH", "")
PATH = f"{VIRTUAL_ENV}/bin:{_OLD_VIRTUAL_PATH}"
os.environ["PATH"] = PATH

# Unset PYTHONHOME if set
if "PYTHONHOME" in os.environ:
    _OLD_VIRTUAL_PYTHONHOME = os.environ["PYTHONHOME"]
    del os.environ["PYTHONHOME"]

if not os.environ.get("VIRTUAL_ENV_DISABLE_PROMPT"):
    _OLD_VIRTUAL_PS1 = os.environ.get("PS1", "")
    PS1 = f"(venv) {_OLD_VIRTUAL_PS1}"
    os.environ["PS1"] = PS1
    VIRTUAL_ENV_PROMPT = "(venv) "
    os.environ["VIRTUAL_ENV_PROMPT"] = VIRTUAL_ENV_PROMPT
