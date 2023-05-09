import re


def print_welcome_message():
    print(
        """
      *******  Welcome to The MadLib Game!! *******  
      A series of questions will be asked. 

        Please answer all questions

      """
    )


def read_template(location_of_file):
    """
    INPUT >> path to file
    OUTPUT >> raw string of everything in file
    """
    try:
        with open(location_of_file, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError as fnf_error:
        print("An error was encountered when grabbing a file")
        print(fnf_error)
        raise FileNotFoundError


def parse_template(string):
    """
    INPUT >> raw string from read_template function
    OUTPUT >> tuple with two parts
        - stripped string
        - a tuple with the values taken out
    """

    pattern = r"\{([\w\s\d\'\-]+)\}"
    words_list = re.findall(pattern, string)
    words_tuple = tuple(words_list)

    replace = r"\{([\w\s\d\'\-]+)\}"
    new_string = re.sub(replace, "{}", string)

    return (new_string, words_tuple)


def merge(string, user_input):
    """
    INPUTS
      - the template string
      - a tuple with user input
    OUTPUT >> a combined string
    """

    merged_string = string.format(*user_input)
    return merged_string


def ask_user_questions(words_tuple):
    """
    INPUT >> tuple - keywords from template
    OUTPUT >> tuple of user answers
    """

    answers = []
    for words in words_tuple:
        response = input(f"Please enter a {words} >> ")
        answers.append(response)

    answer_tuple = tuple(answers)
    return answer_tuple


def save_file(final):
    with open("../assets/users_custom_file.txt", "w") as new_file:
        new_file.write(final)


def initialize(template_path):
    print_welcome_message()
    raw_template = read_template(template_path)
    stripped_string, key_words = parse_template(raw_template)
    user_response = ask_user_questions(key_words)
    merged_user_input = merge(stripped_string, user_response)

    print(merged_user_input)
    save_file(merged_user_input)


if __name__ == "__main__":
    initialize("../assets/dark_and_stormy_night_template.txt")