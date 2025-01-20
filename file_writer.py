# Create a program that attempts to open a file in append mode and write a string to it. 
# If the file doesn't exist, catch the exception and create the file. 
# Additionally, ensure that the file is closed, whether or not the operation was successful.

def write_to_file(file_path: str, text_to_add: str) -> str:
    file = None
    content = ""

    try:
        file = open(file_path, 'r+')
    except FileNotFoundError:
        print(f"Ֆայլը չի գտնվել։ Ստեղծում ենք ֆայլ՝ {file_path}")
        file = open(file_path, 'w')
    finally:
        file.write(text_to_add)

        file.close()

    # raise ValueError("ASdhahsdjkahsjkdahkjhdskd")

    return content


if __name__ == "__main__":
    path = input("Enter path: ")
    text = input("Enter text: ")
    num = write_to_file(path, text)
    print(num)