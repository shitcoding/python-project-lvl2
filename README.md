# gendiff script
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Build Status](https://travis-ci.org/shitcoding/python-project-lvl2.svg?branch=master)](https://travis-ci.org/shitcoding/python-project-lvl2)
[![Test Coverage](https://api.codeclimate.com/v1/badges/50e489c5fd8398bb3da4/test_coverage)](https://codeclimate.com/github/shitcoding/python-project-lvl2/test_coverage)

---
Generate diff between two files.

Supported file formats: JSON and YAML.
(.json, .yaml, .yml files)

---
## Usage
```
gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```


---
## Installation and usage

Enter the following command to install gendiff script from Test PyPi package index:
```
pip install -i https://test.pypi.org/simple/ shitcoding-gendiff --extra-index-url https://pypi.org/simple/
```

---

### Installation and usage between two JSON files


before.json:
```
{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22"
}
```

after.json:
```
{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}
```

output:
```
> $ gendiff before.json after.json

{
    host: hexlet.io
  - proxy: 123.234.53.22
  + timeout: 20
  - timeout: 50
  + verbose: True
}
```

[![asciicast](https://asciinema.org/a/8AxRJRap70Dl1p8GlHutgrJGx.svg)](https://asciinema.org/a/8AxRJRap70Dl1p8GlHutgrJGx)


---
### Usage between two YAML files and between JSON and YAML file

before.yaml:
```
---
host: hexlet.io
timeout: 50
proxy: 123.234.53.22
```

after.yaml:
```
---
timeout: 20
verbose: true
host: hexlet.io
```


output:
```
> $ gendiff before.yaml after.yaml

{
    host: hexlet.io
  - proxy: 123.234.53.22
  + timeout: 20
  - timeout: 50
  + verbose: True
}
```
[![asciicast](https://asciinema.org/a/3SHbNtUnJ0bmrNl1iDXYB385I.svg)](https://asciinema.org/a/3SHbNtUnJ0bmrNl1iDXYB385I)


---
