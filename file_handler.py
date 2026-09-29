import pickle


def read_records(filename):

    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file if line.strip()]

    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
        return []

    except PermissionError:
        print(f"Error: Permission denied while reading {filename}.")
        return []

    except OSError as error:
        print(f"Error while reading file: {error}")
        return []


def write_invalid_records(filename, records):

    try:
        with open(filename, "w") as file:
            for record in records:
                file.write(record + "\n")

    except PermissionError:
        print(f"Error: Permission denied while writing {filename}.")

    except OSError as error:
        print(f"Error while writing file: {error}")


def save_records(filename, records):

    try:
        with open(filename, "wb") as file:
            pickle.dump(records, file)

    except PermissionError:
        print(f"Error: Permission denied while creating {filename}.")

    except OSError as error:
        print(f"Error while saving pickle file: {error}")


def load_records(filename):

    try:
        with open(filename, "rb") as file:
            return pickle.load(file)

    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
        return []

    except (pickle.PickleError, EOFError):
        print("Error: Could not read the pickle data.")
        return []

    except OSError as error:
        print(f"Error while loading pickle file: {error}")
        return []