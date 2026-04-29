def clean_text(text):
    return text.strip().lower()


def is_valid(text):
    return text and len(text.strip()) >= 5
