from cs50 import get_string


def main():
    text = get_string("Text: ")
    grade_level = 0.0588 * L_counter(text) - 0.296 * S_counter(text) - 15.8

    if grade_level < 1:
        print("Before Grade 1")

    elif grade_level > 15:
        print("Grade 16+")

    else:
        print(f"Grade {round(grade_level)}")


def L_counter(text):
    return (100 * (letters(text) / words(text)))


def S_counter(text):
    return (100 * (sentences(text) / words(text)))


def letters(text):
    no_letters = 0
    for i in text:
        if i.isalpha():
            no_letters += 1
    return no_letters


def sentences(text):
    no_sentences = 0
    for i in text:
        if (i == "." or i == "!" or i == "?"):
            no_sentences += 1
    return no_sentences


def words(text):
    no_spaces = 0
    for i in text:
        if i == ' ':
            no_spaces += 1
    return (no_spaces + 1)


main()
