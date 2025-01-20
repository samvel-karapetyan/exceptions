# File Handling with Try-Except
# Create a program that attempts to open and read from a file. 
# If the file does not exist, catch the exception and print a message. 
# Additionally, ensure that the file is closed.

def read_file_to_int(file_path: str) -> str:
    """
    ...
    """
    file = None
    content = ""

    try:
        file = open(file_path, 'r')
        content = file.read()
        
        content = int(content)
    except FileNotFoundError:
        print("Ֆայլը չի գտնվել։")
    except ValueError:
        print(f"{content} թիվ չի դառնում")
    # else, finally
    finally:
        if file:
            file.close()


    return content


if __name__ == "__main__":
    path = input("Enter path: ")
    num = read_file_to_int(path)
    print(num)