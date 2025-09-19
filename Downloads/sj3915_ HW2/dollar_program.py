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
    
   
   
    
    dollar_pattern = r'''
        (?:
   
            (?:(?:US\s*)?\$|USD\s*|(?:US|American|Canadian|Australian)\s+dollars?\s+)\s*
            \d{1,3}(?:,\d{3})*(?:\.\d{1,2})?\s*(?:million|billion|trillion|thousand)?
        |
            
            \d{1,3}(?:,\d{3})*(?:\.\d{1,2})?\s*(?:million|billion|trillion|thousand)?\s+
            (?:US\s+)?dollars?(?!\s+and)
        |
            
            (?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion)
            (?:\s+(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion))*
            \s+(?:US\s+)?dollars?
        |
            
            \d{1,3}(?:,\d{3})*(?:\.\d{1,2})?\s+(?:US\s+)?dollars?\s+and\s+\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?\s+cents?
        |
            
            (?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion)
            (?:\s+(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion))*
            \s+(?:US\s+)?dollars?\s+and\s+
            (?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion)
            (?:\s+(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion))*
            \s+cents?
        |
            
            \d{1,3}(?:,\d{3})*(?:\.\d{1,2})?\s+cents?
        |
            
            (?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion)
            (?:\s+(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand|million|billion|trillion))*
            \s+cents?
        |
            
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
    

    with open('dollar_output.txt', 'w', encoding='utf-8') as output_file:
        for match in matches:
            output_file.write(match + '\n')
            print(match)  

    print(f"\nFound {len(matches)} dollar amounts. Results saved to dollar_output.txt")

if __name__ == "__main__":
    main()