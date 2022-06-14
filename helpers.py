def format_and_clean_text(text):
    return "".join(
        [
            char
            for char in text
            if (
                char.isalpha()
                or char == " "
                or char == "."
                or char == ":"
                or char == "-"
                or char == "\u2013"
            )
        ]
    )
