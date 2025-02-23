# John Rey Bulfa
# ITELEC2
# Laboratory #19 – Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

def get_sentence_input() -> str:
    return input("Enter a sentence: ")
def count_words(sentence: str) -> int:
    words = sentence.split()
    return len(words)
def main():
    sentence = get_sentence_input()
    word_count = count_words(sentence)
    print(f"The sentence has {word_count} words.")
if __name__ == "__main__":
    main()