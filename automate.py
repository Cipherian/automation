import re


def read_file(path: str):
    try:
        with open(path, "r") as f:
            return f.read()

    except FileNotFoundError:
        raise FileNotFoundError(f"File {path} not found")

def remove_dupes(text: list[str]):
    return list(set(text))


def find_emails(text: str):
    # useful regex https://stackoverflow.com/questions/67423037/python-extract-email-address-from-a-huge-string
    email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
    no_dup_emails = remove_dupes(email)

    return no_dup_emails


def phone_format(phone_number: str):
    # https://stackoverflow.com/questions/7058120/whats-the-best-way-to-format-a-phone-number-in-python
    return format(int(phone_number[:-1]), ",").replace(",", "-") + phone_number[-1]


def find_phone_numbers(text: str) -> list[str]:
    phone_numbers_regex = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}\d', text)
    no_dup = remove_dupes(phone_numbers_regex)
    stripped_numbers = []
    for phone_number in no_dup:
        clean_one = phone_number.replace('+', '')
        clean_two = clean_one.replace('(', '')
        clean_three = clean_two.replace(')', '')
        clean_four = clean_three.replace('.', '')
        clean_five = clean_four.replace('-', '')
        stripped_numbers.append(phone_format(clean_five))

    return stripped_numbers


def write_data(text: list[str], output_path: str):
    with open(output_path, "a") as f:
        for line in text:
            f.write(line + "\n")


if __name__ == "__main__":
    text_content = read_file('assets/content.txt')
    emails = find_emails(text_content)
    phone_numbers = find_phone_numbers(text_content)
    write_data(emails, 'assets/emails.txt')
    write_data(phone_numbers, 'assets/phone_numbers.txt')
