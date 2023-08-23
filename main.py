import sys
from numeral import roman_to_numeral, numeral_to_roman
import argparse

if __name__ == '__main__':
    """Convert a Roman numeral to a number or a number to a Roman numeral.
    
    Usage:
    python main.py roman <roman numeral>
    python main.py numeral <number>
    
    Examples:
    python main.py roman MCMXCIX
    python main.py numeral 1999
    
    Keyword arguments:
    roman -- the Roman numeral to convert
    number -- the number to convert

    Flags:
    -S, --silent -- only print the result
    
    Returns:
    The number represented by the Roman numeral or the Roman numeral represented by the number
    
    """

    parser = argparse.ArgumentParser(
        prog='Roman Numeral Converter',
        description='Convert a Roman numeral to a number or a number to a Roman numeral.',
        epilog='Example: python main.py roman MCMXCIX'
    )

    parser.add_argument('type', help='The type of conversion to perform', choices=['roman', 'numeral'])
    parser.add_argument('value', help='The value to convert')
    parser.add_argument('-S', '--silent', help='Only print the result', action='store_true')

    args = parser.parse_args()

    if args.type == 'roman':
        try:
            result = roman_to_numeral(args.value)
            if not args.silent:
                print(f"{args.value} = {result}")
            else:
                print(result)
        except ValueError:
            print(f"Invalid Roman numeral: {args.value}", file=sys.stderr)
    elif args.type == 'numeral':
        try:
            result = numeral_to_roman(int(args.value))
            if not args.silent:
                print(f"{args.value} = {result}")
            else:
                print(result)
        except ValueError:
            print(f"Invalid number: {args.value}", file=sys.stderr)
