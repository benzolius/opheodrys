# opheodrys
Flexible configuration system for Python projects

## Purpose

The purpose of the project is to have a flexible configuration system.

For now the config files should be YAML files (yaml.org)

### default.yaml
Usually there should be sensible default values, which can be saved in a source
control management system (SCM)

### custom.yaml
Usually there are local custom values, which shouldn't be saved in a source
control management system (SCM)

#### Features

* The package loads the objects from yaml files and merges the values in the
  following way:

  Values from the default.yaml are loaded into the result object.
  Values from the custom.yaml are loaded too and will owerwrite values from default.yaml.


## Requirements

* gnu/Linux
* Python 3

* Pyyaml


## Installation

pip install git+https://github.com/benzolius/opheodrys.git
