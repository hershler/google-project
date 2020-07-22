from complete_to_sentences import init_system, find_best_k_completions


if __name__ == "__main__":
    print("starting...\n")
    init_system()
    print("finished\n")
    while True:
        input_ = input("please")
        while input_[-1] != '#':
            # validate_input()
            completions = find_best_k_completions(input_)
            print(f"completions: {completions}\n{input_}", end="")
            input_ += input()


