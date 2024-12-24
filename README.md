# XCString-converter
Convert xcstrings files to key value strings, translate them in ChatGPT or Claude then add them back into xcstring file


A Python utility for managing iOS/macOS localization files (.xcstrings). This tool simplifies the workflow of extracting strings for translation and updating the xcstrings file with new translations.

## Features

- Extract English strings from xcstrings file into a simple key-value format
- Update xcstrings file with translations for any target language
- Preserves existing xcstrings file structure and metadata
- Handles string escaping and complex formatting

## Requirements

- Python 3.6 or higher

## Installation

Clone this repository:
```bash
git clone https://github.com/yourusername/xcstrings-converter.git
cd xcstrings-converter
```

## Usage

### Extracting English Strings

To extract strings from your xcstrings file:

```bash
python xcstrings_converter.py extract Localizable.xcstrings english_strings.txt
```

This will create a file with strings in the format:
```
"key" = "english value"
```

### Adding Translations

1. Create a new file with your translations using the same format:
```
"key" = "translated value"
```

2. Update the xcstrings file with your translations:
```bash
python xcstrings_converter.py update Localizable.xcstrings translated_strings.txt language-code
```

Replace `language-code` with the appropriate code for your target language.

### Common Language Codes

- German: de
- French: fr
- Spanish: es
- Italian: it
- Japanese: ja
- Korean: ko
- Simplified Chinese: zh-Hans
- Traditional Chinese: zh-Hant

## Example Workflow

1. Extract English strings:
```bash
python xcstrings_converter.py extract Localizable.xcstrings english_strings.txt
```

2. Send `english_strings.txt` for translation

3. Receive translated file (e.g., `german_strings.txt`) and update xcstrings:
```bash
python xcstrings_converter.py update Localizable.xcstrings german_strings.txt de
```

## Command Line Arguments

### Extract Command
```bash
python xcstrings_converter.py extract <xcstrings_file> <output_file>
```

- `xcstrings_file`: Path to your source xcstrings file
- `output_file`: Where to save the extracted strings

### Update Command
```bash
python xcstrings_converter.py update <xcstrings_file> <translations_file> <language_code> [--output output_file]
```

- `xcstrings_file`: Path to your source xcstrings file
- `translations_file`: File containing translated strings
- `language_code`: Target language code (e.g., de, fr, es)
- `--output`: Optional. Path for the output file. If not specified, updates the source file

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
