from complete_to_sentences import init_system, find_best_k_completions
from utils import normal_string, detailed_completion


def print_completions(the_completions):
    m = len(the_completions)

    if not the_completions:
        print("no suggestions :(")
        return

    print(f"Here are the {m} suggestions\n")
    for i in range(1, m + 1):
        print(f"{i}. {detailed_completion(the_completions[i - 1])}")


def start_app():
    print("Loading the files and preparing the system\n...")
    init_system()
    print("...\nthe system is ready \n")
    input_ = '$'
    while input_:
        input_ = input("please enter a text\n")
        while input_ and input_[-1] != '#':
            normal_input = normal_string(input_)
            if len(normal_input) < 2:
                print("the string to search must have a length of at least 2 letters")
                break
            completions = find_best_k_completions(normal_input)
            print_completions(completions)
            print(input_, end='')
            input_ += input()
