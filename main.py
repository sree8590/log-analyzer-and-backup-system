from file_handler import read_records, write_invalid_records, save_records, load_records
from processor import process_records, get_invalid_records

INPUT_FILE = "log.txt"
INVALID_FILE = "invalid_log.txt"
BACKUP_FILE = "valid_records.pkl"


def main():
    
    print("     Secure Log Analyzer & Backup System")
    

    records = read_records(INPUT_FILE)
    if not records:
        print("\nNo records found.")
        return

    valid_records = process_records(records)
    invalid_records = get_invalid_records(records)

    print("\nValid Login Records")
  

    if valid_records:
        for username, email, login_time in valid_records:
            print(f"Username: {username} | Email: {email} | Login Time: {login_time}")
    else:
        print("No valid records found.")

    write_invalid_records(INVALID_FILE, invalid_records)
    print(f"\nInvalid records saved to {INVALID_FILE}")

    save_records(BACKUP_FILE, valid_records)
    print(f"Valid records stored in {BACKUP_FILE}")

    stored_records = load_records(BACKUP_FILE)
    print("\nRecords Loaded From Pickle")
   

    for username, email, login_time in stored_records:
        print(f"Username: {username} | Email: {email} | Login Time: {login_time}")

    print("\nProgram completed successfully.")


if __name__ == "__main__":
    main()