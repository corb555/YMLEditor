import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, \
    QSpacerItem, QSizePolicy

from YMLEditor.settings_widget import SettingsWidget
from YMLEditor.yaml_config import YamlConfig

"""
A sample application that loads  data from a config file, initializes
the SettingsWidget for displaying and editing settings, and provides a save button
and an undo button.
"""


def create_window(settings):
    """
    Creates the main application window with the  settings widget.
    """

    # Create Save button
    max_width = 80
    save_button = QPushButton("Save")
    save_button.clicked.connect(settings.save)
    save_button.setFixedWidth(max_width)

    # Create Undo button
    undo_button = QPushButton("Undo")
    undo_button.clicked.connect(settings.undo)
    undo_button.setFixedWidth(max_width)

    # Create button bar
    button_bar = QHBoxLayout()
    button_bar.addWidget(save_button)
    button_bar.addWidget(undo_button)

    # Set up the display with the settings widget and buttons
    w = QWidget()
    layout = QVBoxLayout()

    layout.addWidget(settings)  # Add the scroll area instead of settings_widget directly
    layout.addLayout(button_bar)
    vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
    layout.addItem(vertical_spacer)

    w.setLayout(layout)
    return w


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the UI layout for the fields in the "tests/sample.yml" file.
    formatsYAML = {
        "layout1": {
            "TIP": ("Tip Amount", "line_edit", r'^\d{1,2}%?$', 50),
            "DESSERT": ("Dessert", "combo", ["Tiramisu", "Apple Tart", "Cheesecake"], 200),
            "HOME": ("Home", "combo", ["A", "B", "C", "D"], 200),
            "SITES.@HOME": ("Preferred", "read_only", None, 180),
            "SITES.B": ("Location B", "line_edit", None, 180),
            "SITES": ("Sites", "line_edit", None, 500),
        },
    }

    # Load file
    config = YamlConfig()
    file = "sample.yml"
    success = config.load(file)
    if not success:
        sys.exit()

    # Create the settings widget to display and edit the YAML settings with our format
    settings_widget = SettingsWidget(config, formatsYAML, "layout1", ["HOME"])

    # Create main window and add settings_widget and buttons
    window = create_window(settings_widget)

    # Display the settings
    settings_widget.display()

    # Test delete and redisplay
    settings_widget.clear_layout()
    settings_widget.display()

    window.show()

    # Start UI event loop
    sys.exit(app.exec())
