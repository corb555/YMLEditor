# Readme


## Overview

`YMLEditor` is a package for validating YAML configuration files.  It  provides a wrapper for reading
and validating YAML files with clean and detailed error messages wrapped around the Cerberus Validator.

## Features

**YamlConfig** provides functionality for creating, loading, updating, and saving YAML files using PyYAML.

- **Load / Save / Create** Provides interfaces to load and save YAML files and to create new YAML files.
- **Get / Set Operations:** Provides simple key/value access to data fields in the YAML configuration, including
scalars (int, float, str, bool, date), lists, and dictionaries.  _Complex  hierarchies are not supported._
- **Undo Support:** Keeps a snapshot for each save _in session_ and restores from stack.
- **Granular Dependency Management:** For build system integration, this can be configured to touch a proxy file 
when a specified field changes, offering more granular dependency tracking for build systems.
- **YAML schema validation** Uses Cerberus schema validator and provides a wrapper to improve error messages.

## Installation

To install `YMLEditor`:
Select the install below depending on whether you want to use PyQt6 or PySide6.  Both have identical functionality.

```bash
pip install YMLEditor[pyqt]  # Installs PyQt6, or:
pip install YMLEditor[pyside]  # Installs PySide6
```

## License

`YMLEditor` is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## NOTES
- Only basic YAML syntax is supported:
- Data type specification tags such as !!int, !!float, etc. are ignored
- Anchors and aliases are not supported
- Comments are stripped

## Source Code Documentation
[Source Documentation](https://htmlpreview.github.io/?https://github.com/corb555/YMLEditor/blob/main/docs/_build/html/index.html)

## Support
To report an issue, please visit the [issue tracker](https://github.com/corb555/YMLEditor/issues).