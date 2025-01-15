# Dataset Prompt Extractor
Dataset Prompt Extractor is a PyQt5-based GUI application designed to extract prompts from files inside a dataset folder. The tool will normalize the text and add `<lora:{chosen-lora}:1>` tag to allow a fast testing of your dataset using sd-webui-forge "Prompts from file or textbox" script.

## Manual installation & Setup
### 1. Clone the Repository
``` bash
git clone https://github.com/ImKyra/DatasetPromptExtractor
cd DatasetPromptExtractor
```
### 2. Run the script
For **Linux/macOS**:
``` bash
./run_gui.sh
```
For **Windows**:
``` bash
.\run_gui.bat
```

## File Structure
``` 
/project-directory
│
├── run.py                  # Main file to run the GUI application
├── run_gui.sh              # Shell script for running the app on Linux/Mac
├── run_gui.bat             # Batch script for running the app on Windows
├── DatasetExtractor.py     # Core processing logic for dataset text files
├── requirements.txt        # Python dependency requirements
└── README.md               # Project documentation
```
## Contributing
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push your branch (`git push origin feature/new-feature`).
5. Submit a pull request.

## License
This project is licensed under the [MIT License]().
