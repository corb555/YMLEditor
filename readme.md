# Readme

<img width="622" alt="sample" src="https://github.com/corb555/YMLEditor/blob/62749ffe58806449d0adba7040e1157ae4b184c2/images/YMLEditor.png?raw=true">

## Overview

`YMLEditor` is a package for easily creating editors for YAML configuration files.  

## Features

**SettingsWidget** provides a Widget for displaying and editing config file fields. You
simply list the fields with their config key and the widget type you want for 
each (line_edit, text_edit, etc.). You can also add a regex for data entry validation. 
The SettingsWiget and YamlConfig  will
read the config file, display the fields for editing, and then save the data.

- **Easy Front-End Creation:** Create a configuration editor with a few lines of code.
- **Configurable Layout:** Displays settings using the format you provide.
- **Input Validation:** Validates input based on supplied regular expressions and 
highlights invalid entries. In the sample above, Tip Amount is highlighted because it contains letters.
- **Data Syncing:** Synchronizes data values between the UI and the config file, seamlessly using the
  ConfigFile manager described below.
- **Utilizes PyQt6 or PySide6**

**Supported Widgets** 

- text_edit - options=regex for validation
- line_edit - options=regex for validation
- read_only - a read-only line_edit
- combo - options=[comboBox items]
- checkbox
- spinbox - floating point spin box.  options=[min, max, step, precision]
- slider - options=[min, max]
- label

**YamlConfig** provides functionality for creating, loading, updating, and saving YAML files using PyYAML.

- **Load / Save / Create** Provides interfaces to load and save YAML files and to create new YAML files.
- **Get / Set Operations:** Provides simple key/value access to data fields in the YAML configuration, including
scalars (int, float, str, bool, date), lists, and dictionaries.  _Complex  hierarchies are not supported._
- **Undo Support:** Keeps a snapshot for each save _in session_ and restores from stack.
- **Granular Dependency Management:** For build system integration, this can be configured to touch a proxy file 
when a specified field changes, offering more granular dependency tracking for build systems.

## Installation

To install `YMLEditor`:
Select the install below depending on whether you want to use PyQt6 or PySide6.  Both have identical functionality.

```bash
pip install YMLEditor[pyqt]  # Installs PyQt6, or:
pip install YMLEditor[pyside]  # Installs PySide6
```

### Format Layout

Each line in the format corresponds to a field in the config file and contains the following:  
`ConfigKey: (DisplayName, WidgetType, Options, Width, <style>)`

- Config Key: The name of the item in the YAML config file
- Display Name: The name to show in the UI.
- Widget Type: The type of input control (see **Supported Widgets** above)
- Options: Either a regex pattern for field validation (e.g., line_edit), 
       or options for the widget
- Field Width: Width of the widget.
- Style: (optional) Contains a QT style for the widget. e.g. "color: slategray;"),

### Sample layout format

```python
formats = {
        "layout1": {
            "TIP": ("Tip Amount", "line_edit", r'^\d{1,2}$', 50),
            "DESSERT": ("Dessert", "combo", ["Tiramisu", "Apple Tart", "Cheesecake"], 200),
            "HOME": ("Home", "combo", ["A", "B", "C", "D"], 200),
            "SITES.@HOME": ("Preferred", "read_only", None, 180, "color: slategray;"),
            "SITES.B": ("Location B", "line_edit", None, 180),
            "SITES": ("Sites", "line_edit", None, 500),
            "BRIGHT": ("Brightness", "slider", [0, 10], 200),
            "EXPERT": ("Expert", "checkbox", None, 200),
            "VALUE": ("Value", "spinbox", [-.5, 1.5, .1, 1], 200),
        },
    }
```
- SITES.@HOME - If '@' is present, that key will be looked up and replace by its contents (SITES.A in this example)
- SITES.B - You can access sub hierarchies by using "." to separate keys (Boston in this example)
- TIP - The regex for Tips highlights entries that aren't 1 or 2 digits.

### Sample YAML file

```yaml
DESSERT: Apple Tart
TIP: 18
HOME: A
SITES:
  A: Albany
  B: Boston
  C: Chicago
BRIGHT: 3
EXPERT: '0'
VALUE: -0.3
  ```

### Sample App

Sample.py is provided to demonstrate the capabilities of `YMLEditor` with a sample YAML file.

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