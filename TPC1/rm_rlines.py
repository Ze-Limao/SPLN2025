import sys

def remove_repeated_lines(input_lines):
    seen = set()
    unique_lines = []
    for line in input_lines:
        if line not in seen or line == '\n':
            unique_lines.append(line)
            seen.add(line)
    return unique_lines

def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file, 'r') as file:
            input_lines = file.readlines()
        unique_lines = remove_repeated_lines(input_lines)
        output_file = input_file.replace('.txt', '_filtered.txt')
        with open(output_file, 'w') as file:
            file.writelines(unique_lines)
    else:
        input_lines = sys.stdin.readlines()
        unique_lines = remove_repeated_lines(input_lines)
        
    print(''.join(unique_lines))

if __name__ == "__main__":
    main()
