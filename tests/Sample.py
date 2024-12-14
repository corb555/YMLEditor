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

def create_window(wn, settings):
    """
    Creates the main application window with the settings widget.
    """
    layout = QVBoxLayout()

    # Create a horizontal button layout for save and undo buttons
    button_bar = QHBoxLayout()

    # Create and add Save button linked to settings.save()
    max_width = 80
    save_button = QPushButton("Save")
    save_button.clicked.connect(settings.save)
    save_button.setFixedWidth(max_width)
    button_bar.addWidget(save_button)

    # Create and add Undo button linked to settings.undo()
    undo_button = QPushButton("Undo")
    undo_button.clicked.connect(settings.undo)
    undo_button.setFixedWidth(max_width)
    button_bar.addWidget(undo_button)

    # Set up the display with the settings widget and buttons
    layout.addWidget(settings)
    layout.addLayout(button_bar)
    vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
    layout.addItem(vertical_spacer)

    wn.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Set background color for read only fields
    # Set other widget colors to your preference here
    app.setStyleSheet(
        f"""
                QLineEdit:read-only {{
                    color:"lightslategray"; 
                    background-color:"#3a3a3a";
                    outline:none; 
                    border:none;
                }}
                """
    )

    # Create the layout for the fields in the "tests/sample.yml" file.
    formatsYAML = {
        "layout1": {
            "TIP": ("Tip Amount", "line_edit", r'^\d{1,2}$', 50),
            "DESSERT": ("Dessert", "combo", ["Tiramisu", "Apple Tart", "Cheesecake"], 200),
            "HOME": ("Home", "combo", ["A", "B", "C", "D"], 200),
            "SITES.@HOME": ("Preferred", "read_only", None, 180),
            "SITES.B": ("Location B", "line_edit", None, 180),
            "SITES": ("Sites", "line_edit", None, 500),
        },
    }

    # Load YAML config file
    config = YamlConfig()
    file = "sample.yml"
    success = config.load(file)
    if not success:
        sys.exit()

    w = QWidget()

    # Create a settings widget to display and edit the YAML settings with our format
    settings_widget = SettingsWidget(config, formatsYAML, "layout1", ["HOME"])

    # Create main window and add the settings_widget and buttons
    create_window(w, settings_widget)

    # Display the settings
    settings_widget.display()
    w.show()

    # Start QT event loop
    sys.exit(app.exec())

