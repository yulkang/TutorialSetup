import os
from pylabyk.localfile import mkdir4file


def add_string_to_file(input_file, output_file, string_to_add):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        print(f'original content of {input_file}: {content}')
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return

    content += string_to_add
    print(f'Modified content: {content}')

    try:
        mkdir4file(file)
        with open(output_file, 'x') as file:
            file.write(content)
        print(f"Modified content has been written to '{output_file}'.")
    except:
        print("Error occurred while writing to the output file.")
        raise


def main():
    print(os.getcwd())
    add_string_to_file(
        '../../Data_TutorialSetup/TutorialSetup/src/author1_2023/example.txt',
        '../../Data_TutorialSetup/TutorialSetup/res/author1_2023/example_output.txt',
        ' - read by main_author1_2023.py'
    )

if __name__ == '__main__':
    main()