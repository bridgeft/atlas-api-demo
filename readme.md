# Atlas API Demo

This repository demonstrates consuming the Atlas API via Python. To get started you'll need the latest version of python:

- [For windows](https://www.python.org/downloads/windows/)
- [For mac](https://www.python.org/downloads/macos/)
- [For linux](https://www.python.org/downloads/source/)
- [Other platforms](https://www.python.org/download/other/)



## Setup

Clone the repository with git:

```
git clone git@bridgeft.com/atlas-api-demo
```

You should create a virtual environment by running:

```python
python3 -m venv /path/to/venv
```

For example:

```python
cd atlas-api-demo
python3 -m venv venv/
```

Activate the virutal environment and install the project requirements:

```shell
source venv/bin/activate
pip install -r requirements.txt
```



## Configuration

Copy the `.dev-templates/env.template` to `.env`:

```shell
# navigate to your atlas-api-demo top level directory
cd /path/to/atlas-api-demo
cp .dev-templates/env.template .env

# fill in environment variables, then source it
source .env
```

Set the `PYTHONPATH` to the top-level location of the atlas-api-demo, and update your environment variables by running `source .env`

