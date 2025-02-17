import sys
import argparse

def remove_repeated_lines(input_lines, spaces, comment):
    seen = set()
    unique_lines = []
    for line in input_lines:
        stripline = line.rstrip('\n')
        if not spaces:
            stripline = line.strip()
        if stripline not in seen:
            if comment and stripline == '':
                unique_lines.append('#\n')
            else:
                unique_lines.append(line)
                seen.add(stripline)
    return unique_lines

def main():
    parser = argparse.ArgumentParser(description="Remove repeated lines.")
    parser.add_argument('input_file', nargs='?', help="Input file (default: stdin)")
    parser.add_argument('-s', '--spaces', action='store_true', help="Consider spaces in line comparison")
    parser.add_argument('-p', '--comment', action='store_true', help="Comment empty lines with #")
    args = parser.parse_args()
    if args.input_file:
        with open(args.input_file, 'r') as file:
            input_lines = file.readlines()
        unique_lines = remove_repeated_lines(input_lines, args.spaces, args.comment)
    else:
        input_lines = sys.stdin.readlines()
        unique_lines = remove_repeated_lines(input_lines, args.spaces, args.comment)

    print(''.join(unique_lines))
    if args.input_file:
        output_file = args.input_file.replace('.txt', '_filtered.txt')
    else:
        output_file = 'filtered.txt'
    with open(output_file, 'w') as file:
        file.writelines(unique_lines)

if __name__ == "__main__":
    main()
