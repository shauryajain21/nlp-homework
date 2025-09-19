
import re
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python telephone_program.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    
    phone_pattern = r'''
        (?:

            (?:\+1[\s\-\.]?)?
            \(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]\d{4}
        |

            \(\d{3}\)[\s\-\.]?\d{3}[\s\-\.]\d{4}
        |

            \d{3}[\s\-\.]\d{3}[\s\-\.]\d{4}
        |

            (?<!\d)\d{10}(?!\d)
        |

            \d{3}[\s\-\.]\d{4}
        |

            \+1[\s\-\.]\d{3}[\s\-\.]\d{3}[\s\-\.]\d{4}
        |

            \(\d{3}\)[\s\-\.]?\d{3}[\s\-\.]\d{4}
        |

            \d{3}[\s\-\.]\d{3}[\s\-\.]\d{4}
        |

            (?<!\d)\d{3}[\s\-\.]\d{4}(?!\d)
        |

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

                        if not re.match(r'^[0\-\.\s\(\)]+$', cleaned_match):
                            matches.append(cleaned_match)
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    

    for match in matches:
        print(match)

if __name__ == "__main__":
    main()