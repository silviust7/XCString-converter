import json
import argparse

def extract_english_strings(xcstrings_path, output_path):
    """
    Extract English strings from xcstrings file and save them in a simple key=value format
    """
    with open(xcstrings_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    strings = {}
    for key, value in data.get('strings', {}).items():
        # Get the English translation from the sourceLanguage
        english_text = value.get('localizations', {}).get('en', {}).get('stringUnit', {}).get('value', '')
        
        # If not found in localizations, try variations
        if not english_text:
            try:
                english_text = value.get('strings', {}).get('en', '')
            except AttributeError:
                pass
        
        if english_text:
            strings[key] = english_text
    
    # Write to file in "key" = "value" format
    with open(output_path, 'w', encoding='utf-8') as f:
        for key, value in strings.items():
            # Escape quotes in the value
            value = value.replace('"', '\\"')
            f.write(f'"{key}" = "{value}"\n')

def update_xcstrings_with_translations(xcstrings_path, translations_path, language_code, output_path=None):
    """
    Update xcstrings file with translations for a specific language
    translations_path should contain strings in "key" = "value" format
    """
    # Read original xcstrings file
    with open(xcstrings_path, 'r', encoding='utf-8') as f:
        xcstrings_data = json.load(f)
    
    # Read translations
    translations = {}
    with open(translations_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and '=' in line:
                try:
                    key, value = [part.strip().strip('"').replace('\\"', '"') for part in line.split('=', 1)]
                    translations[key] = value
                except Exception as e:
                    print(f"Warning: Couldn't parse line: {line}")
                    continue
    
    # Update xcstrings data with translations
    for key, value in translations.items():
        if key in xcstrings_data.get('strings', {}):
            if 'localizations' not in xcstrings_data['strings'][key]:
                xcstrings_data['strings'][key]['localizations'] = {}
            
            xcstrings_data['strings'][key]['localizations'][language_code] = {
                'stringUnit': {
                    'state': 'translated',
                    'value': value
                }
            }
    
    # Write updated xcstrings file
    output_path = output_path or xcstrings_path
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(xcstrings_data, f, indent=2, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser(description='XCStrings Converter Tool')
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Extract command
    extract_parser = subparsers.add_parser('extract', help='Extract English strings')
    extract_parser.add_argument('xcstrings_file', help='Input xcstrings file')
    extract_parser.add_argument('output_file', help='Output file for English strings')
    
    # Update command
    update_parser = subparsers.add_parser('update', help='Update xcstrings with translations')
    update_parser.add_argument('xcstrings_file', help='Original xcstrings file')
    update_parser.add_argument('translations_file', help='File containing translations')
    update_parser.add_argument('language_code', help='Language code (e.g., fr, es)')
    update_parser.add_argument('--output', help='Output xcstrings file (optional)')
    
    args = parser.parse_args()
    
    if args.command == 'extract':
        extract_english_strings(args.xcstrings_file, args.output_file)
        print(f'English strings extracted to {args.output_file}')
    
    elif args.command == 'update':
        update_xcstrings_with_translations(
            args.xcstrings_file,
            args.translations_file,
            args.language_code,
            args.output
        )
        output = args.output or args.xcstrings_file
        print(f'Updated xcstrings file saved to {output}')

if __name__ == '__main__':
    main()
