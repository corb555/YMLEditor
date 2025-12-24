# yaml_syntax_highlighter.py
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter

class YamlHighlighter(QSyntaxHighlighter):
    """
    A syntax highlighter for YAML files that can also highlight a single line for errors.
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.error_line = -1  # Line number (1-based) of the error

        # --- Standard YAML Syntax Rules ---
        self.highlighting_rules = []

        # Rule for keys (e.g., "key:")
        key_format = QTextCharFormat()
        key_format.setForeground(QColor("#9CDCFE")) # Light Blue
        key_format.setFontWeight(QFont.Bold)
        self.highlighting_rules.append((QRegularExpression(r"^\s*([a-zA-Z0-9_-]+):"), key_format))

        # Rule for comments (e.g., "# a comment")
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6A9955")) # Green
        self.highlighting_rules.append((QRegularExpression(r"#[^\n]*"), comment_format))

        # Rule for string values in quotes
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#CE9178")) # Orange
        self.highlighting_rules.append((QRegularExpression(r"(\".*\"|\'.*\')"), string_format))

        # --- Error Highlighting Rule ---
        self.error_format = QTextCharFormat()
        self.error_format.setBackground(QColor("#5A1D1D")) # Dark Red background

    def set_error_line(self, line_number: int | None):
        """
        Sets the line number to be highlighted as an error.
        Pass None or -1 to clear the error highlight.
        """
        self.error_line = line_number if line_number is not None else -1
        # We must re-highlight the entire document for the change to take effect.
        self.rehighlight()

    def highlightBlock(self, text: str):
        """
        This method is called by Qt for each line of text to apply formatting.
        """
        # --- Check for Error First ---
        # blockNumber() is 0-based, our line numbers are 1-based.
        current_line_number = self.currentBlock().blockNumber() + 1
        if self.error_line == current_line_number:
            self.setFormat(0, len(text), self.error_format)
            return # Stop further processing for this line if it's an error

        # --- Apply Standard Syntax Highlighting ---
        for pattern, format in self.highlighting_rules:
            expression = QRegularExpression(pattern)
            it = expression.globalMatch(text)
            while it.hasNext():
                match = it.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)