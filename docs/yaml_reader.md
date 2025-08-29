
# YAMLLoader: A Robust YAML Loader and Validator

## Overview

`YAMLLoader` is a Python utility class designed to safely load and **validate** YAML configuration files. It provides a robust wrapper around the 
standard `PyYAML` and `Cerberus` libraries, ensuring that your configuration is not only loaded correctly but is also structurally valid.

Its primary purpose: 
* Provide **clear, human-readable, and actionable feedback** when validation fails, transforming cryptic error messages into 
helpful suggestions.
* Add support for including other shared YAML files

## Key Benefits

*   **Schema-Driven Validation:** Define a "data contract" for your configuration files using a Cerberus schema. `YAMLLoader` ensures that all loaded 
configurations are complete and correct before your application's core logic ever sees them.
*   **Human-Friendly Error Reporting:** Instead of just telling a user *that* their configuration is wrong, the loader tells them *what* is wrong, *where* 
it's wrong, and *how to fix it*.
    > **Sample Error Message:**
    > ```
    >   - Problem: The required setting 'min' is missing.
    >     Value Found: None
    >     Location: in the 'scaling' section
    >     Suggestion: Please add 'min: <value>' to this section.
    > ```
*   **Support for `!include`:** Keep your configurations DRY (Don't Repeat Yourself) by including shared settings from other files. The loader automatically 
handles file merging.
*   **Fail-Fast Design:** The loader raises a single, clear `ValueError` containing all formatted errors if a configuration is invalid, allowing your 
application to halt safely instead of proceeding with corrupt data.

## `!include` for Shared Configurations

`YAMLLoader` adds support for a custom `!include` tag, allowing one YAML file to merge settings from another. This is ideal for complex pipelines where 
multiple tools need to share a common set of parameters.

The loader is context-aware and resolves file paths relative to the file in which the tag is used.

### Pattern 1: Simple Include

The contents of the included file are placed directly under the key where `!include` is used.

**`config/shared_columns.yml`:**
```yaml
item_id: node_id
score: importance_score
```

**`config/main.yml`:**
```yaml
# The dictionary from shared_columns.yml will become the value for the column_names key.
column_names: !include shared_columns.yml
output_format: "csv"
```

### Pattern 2: Advanced Merge with Anchors

For more complex cases, you can combine `!include` with standard YAML **anchors (`&`)** and **merge keys (`<<:`)** to merge a shared block at the top level.

**`config/peaks_definition.yml`:**
```yaml
# The &shared_settings is a YAML anchor.
shared_peak_settings: &shared_settings
  column_names:
    item_id: node_id
  extraction_keys:
    natural:
      - peak
```

**`config/peaks_extract.yml`:**
```
# The !include tag loads the file.
imports: !include peaks_definition.yml

# The '<<:' key merges the dictionary referenced by the '*shared_settings' alias.
<<: *shared_settings

# This key will override any identically named key from the included file.
output_format: "csv"
```

## When to Use `YAMLLoader`

`YAMLLoader` is the ideal choice for any application where configuration files are intended to be read or modified by humans. While a simple 
`yaml.safe_load()` is sufficient for internal, machine-generated files, `YAMLLoader` is designed for the "human in the loop," ensuring that when 
configuration errors inevitably happen, they are easy to diagnose and quick to fix.