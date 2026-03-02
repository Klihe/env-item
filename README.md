# ENV-Item

## Description

env-item is a lightweight Python package for working with environment configuration items. 

It provides a simple API to define, access, and manage environment values in Python applications. The core aim is to make environment interaction clear and explicit while fitting seamlessly into modern Python projects.

## Installation

```bash
pip install env-item
```

or

```bash
uv add env-item
```

## Usage

### Importing

```python
from env_item import EnvItem
```

### Basic

```python
from env_item import EnvItem
from dotenv import load_dotenv

load_dotenv()

var = EnvItem("MY_ENV_VAR").as_str()
print(var)
```

### Advenced

```python
from env_item import EnvItem
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = EnvItem("DEBUG").default(False).as_bool()

    class Database:
        HOST = EnvItem("DB_HOST").default("localhost").as_str()
        PORT = EnvItem("DB_PORT").default(5432).as_int()
        USER = EnvItem("DB_USER").required().as_str()
        PASSWORD = EnvItem("DB_PASSWORD").required().secret().as_str()
        NAME = EnvItem("DB_NAME").required().as_str()
    
    class API:
        KEY = EnvItem("API_KEY").required().secret().as_str()
        TIMEOUT = EnvItem("API_TIMEOUT").default(30).as_int()

print(Config.DEBUG)
print(Config.Database.HOST)
print(Config.Database.PORT)
print(Config.Database.USER)
print(Config.Database.PASSWORD) # This will not print the value because it is marked as secret; the value is replaced with ******
print(Config.Database.NAME)
print(Config.API.KEY)
print(Config.API.TIMEOUT)

```

### Constrains

#### required
if variable is not set, it will raise an error.
```python
VAR = EnvItem("MY_ENV_VAR").required()
```

#### default
if variable is not set, it will return the default value.
```python
VAR = EnvItem("MY_ENV_VAR").default("default_value")
```

#### secret
if variable is marked as secret, it will not be printed in logs or error messages.
```python
VAR = EnvItem("MY_ENV_VAR").secret()
```

### Get value

#### as_str
```python
VAR = EnvItem("MY_ENV_VAR").as_str()
print(VAR)
```

#### as_int
```python
VAR = EnvItem("MY_ENV_VAR").as_int()
print(VAR)
```

#### as_bool
```python
VAR = EnvItem("MY_ENV_VAR").as_bool()
print(VAR)
```