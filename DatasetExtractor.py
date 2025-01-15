import os
from PyQt5.QtWidgets import QMessageBox


class DatasetExtractor:

    @staticmethod
    def process(lora_filename, folder, parent=None):
        try:
            # Step 1: Validate folder existence
            if not os.path.exists(folder):
                QMessageBox.critical(
                    parent,
                    "Error",
                    f"The specified folder does not exist: {folder}",
                )
                print(f"[DEBUG] Folder not found: {folder}")
                return ""

            print(f"[DEBUG] Folder found: {folder}")

            # Step 2: List all files and normalize paths
            all_files = os.listdir(folder)  # List all items in folder
            print(f"[DEBUG] All files in folder: {all_files}")

            text_files = []
            for f in all_files:
                # Normalize and debug paths
                abs_path = os.path.join(folder, f)
                print(f"[DEBUG] Checking file: {f}, Full Path: {abs_path}")

                if f.endswith(".txt") and os.path.isfile(abs_path):
                    text_files.append(f)

            if not text_files:
                QMessageBox.warning(
                    parent,
                    "Error",
                    "No .txt files were found in the specified folder.",
                )
                print(f"[DEBUG] No text files found after filtering. Folder: {folder}")
                return ""

            print(f"[DEBUG] Text files found: {text_files}")

            # Step 3: Process each text file
            processed_texts = []  # To store processed texts
            for text_file in text_files:
                file_path = os.path.join(folder, text_file)  # Full file path
                print(f"[DEBUG] Processing file: {file_path}")

                # Read the contents of the file
                with open(file_path, "r", encoding="utf-8") as file:
                    file_content = file.read()

                # Remove all newline characters (\r, \n, and \r\n)
                cleaned_content = file_content.replace("\r\n", "").replace("\r", "").replace("\n", "")

                # Append LORA tag to the text (if required)
                processed_content = cleaned_content + f"<lora:{lora_filename}:1>"
                processed_texts.append(processed_content)

            # Step 4: Combine all processed texts, separated by two carriage returns
            final_output = "\n\n".join(processed_texts)

            print(f"[DEBUG] Final output generated successfully.")

            # Step 5: Show messagebox with a confirmation of success
            QMessageBox.information(
                parent,
                "Processing Done",
                "All text files have been processed successfully.",
            )

            # Return the processed result
            return final_output

        except Exception as e:
            # Handle unexpected errors and show an error dialog
            print(f"[DEBUG] Exception occurred: {str(e)}")
            QMessageBox.critical(
                parent,
                "Error",
                f"An unexpected error occurred:\n{str(e)}",
            )
            return ""
