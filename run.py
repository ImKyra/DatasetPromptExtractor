from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QMessageBox, QLabel, QVBoxLayout,
    QPushButton, QTextEdit, QWidget, QHBoxLayout, QFrame, QScrollArea
)
import os
from DatasetExtractor import DatasetExtractor


class MainWindow(QMainWindow):
    def create_horizontal_layout(self, label_text, button_callback):
        label = QLabel(f"{label_text}:")
        textbox = QTextEdit()
        textbox.setFixedHeight(30)
        button = QPushButton("...")
        button.clicked.connect(button_callback)
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(textbox)
        layout.addWidget(button)
        if label_text == "Dataset Folder":
            self.folder_textbox = textbox
        elif label_text == "LORA File":
            self.file_textbox = textbox
        return layout
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dataset Prompt Extractor")
        self.setGeometry(100, 100, 800, 600)  # Main window dimensions

        # Main layout widget
        self.central_widget = QWidget()
        self.main_layout = QVBoxLayout(self.central_widget)
        self.setCentralWidget(self.central_widget)

        # Folder browser section
        self.folder_layout = self.create_horizontal_layout("Dataset Folder", self.open_folder)

        # File browser section
        self.file_layout = self.create_horizontal_layout("LORA File", self.open_file)

        # Horizontal layout for top section
        top_layout = QVBoxLayout()
        top_layout.addLayout(self.folder_layout)
        top_layout.addLayout(self.file_layout)

        # Processed output section
        self.output_label = QLabel("Processed Output:")
        self.output_textbox = QTextEdit()
        self.output_textbox.setReadOnly(True)  # Output textbox is read-only

        # Buttons
        self.process_button = QPushButton("Process")
        self.clipboard_button = QPushButton("Copy to Clipboard (CC)")
        self.clipboard_button.setStyleSheet("background-color: orange; color: white;")
        self.clipboard_button.clicked.connect(self.copy_to_clipboard)
        self.process_button.setStyleSheet("background-color: green; color: white;")
        self.process_button.clicked.connect(self.process_data)

        self.save_button = QPushButton("Save Output")
        self.save_button.setStyleSheet("background-color: blue; color: white;")
        self.save_button.clicked.connect(self.save_output)

        # Bottom button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.process_button)
        button_layout.addWidget(self.clipboard_button)
        button_layout.addWidget(self.save_button)

        # Add sections to the main layout
        self.main_layout.addLayout(top_layout)
        self.main_layout.addWidget(self.output_label)
        self.main_layout.addWidget(self.output_textbox)
        self.main_layout.addLayout(button_layout)

    def open_folder(self):
        # Open folder browser
        folder_path = QFileDialog.getExistingDirectory(self, "Select Dataset Folder")
        if folder_path:
            self.folder_textbox.setText(folder_path)

    def open_file(self):
        # Open file browser
        file_path, _ = QFileDialog.getOpenFileName(self, "Select LORA File", "", "All Files (*)")
        if file_path:
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            self.file_textbox.setText(file_name)

    def process_data(self):
        # Retrieve inputs
        folder = self.folder_textbox.toPlainText().strip()
        lora_filename = self.file_textbox.toPlainText().strip()

        print(f"[DEBUG] Folder received: {folder}")
        print(f"[DEBUG] LORA file received: {lora_filename}")

        if not folder:
            QMessageBox.critical(self, "Error", "Dataset folder is not selected.")
            print("[DEBUG] Error: Dataset folder is not provided.")
            return
        if not lora_filename:
            QMessageBox.critical(self, "Error", "LORA file is not selected.")
            print("[DEBUG] Error: LORA file is not provided.")
            return

        try:
            # Call DatasetExtractor to process data
            final_output = DatasetExtractor.process(lora_filename, folder)
            print("[DEBUG] Processing completed successfully.")
            self.output_textbox.setText(final_output)
        except Exception as e:
            print(f"[DEBUG] Exception during processing: {str(e)}")
            QMessageBox.critical(self, "Processing Error", f"An error occurred: {str(e)}")

    def save_output(self):
        # Save output to a file
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Output", "", "Text Files (*.txt);;All Files (*)"
        )
        if file_path:
            try:
                content = self.output_textbox.toPlainText()
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(content)
                QMessageBox.information(self, "Success", "Output saved successfully!")
            except Exception as e:
                print(f"[DEBUG] Error saving output: {str(e)}")
                QMessageBox.critical(self, "Save Error", f"An error occurred while saving:\n{str(e)}")

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.output_textbox.toPlainText())
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
