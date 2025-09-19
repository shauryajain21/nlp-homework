#!/usr/bin/env python3
"""
Program to identify telephone numbers in text using regular expressions.
Handles various formats including:
- (555) 123-4567
- 555-123-4567
- 555.123.4567
- 555 123 4567
- 5551234567
- +1 555 123 4567
- With and without area codes
- Different punctuation patterns
"""

import re
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python telephone_program.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Comprehensive regex pattern for telephone numbers
    # This pattern handles various phone number formats
    
    phone_pattern = r'''
        (?:
            # Pattern 1: +1 (555) 123-4567, +1-555-123-4567, etc.
            (?:\+1[\s\-\.]?)?
            \(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]\d{4}
        |
            # Pattern 2: (555) 123-4567, (555)123-4567
            \(\d{3}\)[\s\-\.]?\d{3}[\s\-\.]\d{4}
        |
            # Pattern 3: 555-123-4567, 555.123.4567, 555 123 4567
            \d{3}[\s\-\.]\d{3}[\s\-\.]\d{4}
        |
            # Pattern 4: 5551234567 (10 digit number)
            (?<!\d)\d{10}(?!\d)
        |
            # Pattern 5: 777-1000, 555-HELP (7 digits with separator)
            \d{3}[\s\-\.]\d{4}
        |
            # Pattern 6: International format +1 555 123 4567
            \+1[\s\-\.]\d{3}[\s\-\.]\d{3}[\s\-\.]\d{4}
        |
            # Pattern 7: Parentheses with different separators
            \(\d{3}\)[\s\-\.]?\d{3}[\s\-\.]\d{4}
        |
            # Pattern 8: Area code followed by 7-digit number with various separators
            \d{3}[\s\-\.]\d{3}[\s\-\.]\d{4}
        |
            # Pattern 9: 7-digit numbers without area code
            (?<!\d)\d{3}[\s\-\.]\d{4}(?!\d)
        |
            # Pattern 10: Extensions (basic support)
            (?:\+1[\s\-\.]?)?\(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]\d{4}[\s]*(?:ext|extension|x)[\s]*\d{1,5}
        )
    '''
    
    phone_regex = re.compile(phone_pattern, re.IGNORECASE | re.VERBOSE)
    
    matches = []
    
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line_matches = phone_regex.findall(line)
                for match in line_matches:
                    cleaned_match = match.strip()
                    if cleaned_match:
                        # Basic validation: make sure it's not just zeros or other invalid patterns
                        if not re.match(r'^[0\-\.\s\(\)]+$', cleaned_match):
                            matches.append(cleaned_match)
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    # Print matches to stdout
    for match in matches:
        print(match)

if __name__ == "__main__":
    main()