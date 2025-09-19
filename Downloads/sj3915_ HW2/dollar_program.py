#!/usr/bin/env python3
"""
Program to identify dollar amounts in text using regular expressions.
Handles various formats including:
- $500 million
- $6.57
- 1 dollar and 7 cents
- US dollars, Canadian dollars, etc.
"""

import re
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python dollar_program.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Main regex pattern for dollar amounts - optimized for better performance
    # This single comprehensive pattern handles all dollar amount formats
    
    dollar_pattern = r'''
        (?:
            # Pattern 1: $123.45, $500 million, USD 500, etc.
            (?:(?:US\s*)?\$|USD\s*|(?:US|American|Canadian|Australian)\s+dollars?\s+)\s*
            \d{1,3}(?:,\d{3})*(?:\.\d{1,2})?\s*(?:million|billion|trillion|thousand)?
        |
            # Pattern 2: 123.45 dollars, 500 million dollars, etc.
            \d{1,3}(?:,\d{3})*(?:\.\d{1,2})?\s*(?:million|billion|trillion|thousand)?\s+
            (?:US\s+)?dollars?(?!\s+and)
        |
            # Pattern 3: Written amounts like "five hundred dollars"
            (?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion)
            (?:\s+(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion))*
            \s+(?:US\s+)?dollars?
        |
            # Pattern 4: Mixed format like "1 dollar and 50 cents"
            \d{1,3}(?:,\d{3})*(?:\.\d{1,2})?\s+(?:US\s+)?dollars?\s+and\s+\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?\s+cents?
        |
            # Pattern 5: Written format like "one dollar and fifty cents"
            (?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion)
            (?:\s+(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion))*
            \s+(?:US\s+)?dollars?\s+and\s+
            (?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion)
            (?:\s+(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion))*
            \s+cents?
        |
            # Pattern 6: Cents only
            \d{1,3}(?:,\d{3})*(?:\.\d{1,2})?\s+cents?
        |
            # Pattern 7: Written cents only
            (?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion)
            (?:\s+(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion))*
            \s+cents?
        |
            # Pattern 8: USD at the end
            \d{1,3}(?:,\d{3})*(?:\.\d{1,2})?\s*(?:million|billion|trillion|thousand)?\s+USD
        )
    '''
    
    dollar_regex = re.compile(dollar_pattern, re.IGNORECASE | re.VERBOSE)
    
    matches = []
    
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line_matches = dollar_regex.findall(line)
                for match in line_matches:
                    cleaned_match = match.strip()
                    if cleaned_match:
                        matches.append(cleaned_match)
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    # Write matches to output file
    with open('dollar_output.txt', 'w', encoding='utf-8') as output_file:
        for match in matches:
            output_file.write(match + '\n')
            print(match)  # Also print to stdout

    print(f"\nFound {len(matches)} dollar amounts. Results saved to dollar_output.txt")

if __name__ == "__main__":
    main()