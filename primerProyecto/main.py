import sys
from lexer import tokenize
from parser import parse_tokens


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py input.txt output.txt")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line_number, line in enumerate(infile, 1):
            line = line.strip()
            if not line:
                continue

            outfile.write(f"Oración {line_number}: {line}\n")

            try:
                tokens = tokenize(line)
                outfile.write("  Léxico: OK\n")
                try:
                    parse_tokens(tokens)
                    outfile.write("  Sintáctico: OK\n")
                except Exception as e:
                    outfile.write(f"  Sintáctico: ERROR - {e}\n")
            except Exception as e:
                outfile.write(f"  Léxico: ERROR - {e}\n")

            outfile.write("\n")


if __name__ == "__main__":
    main()
