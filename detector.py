import sys
import os
import time
from kav_python_sdk import scanner, errors

def scan_file(file_path):
    """
    Scan a file for malware using Kaspersky Anti-Virus.
    """
    try:
        scan_result = scanner.scan_file(file_path)
        if scan_result.status == scanner.SCAN_RESULT_OK:
            print("No malware detected.")
        elif scan_result.status == scanner.SCAN_RESULT_INFECTED:
            print("Malware detected:")
            for virus in scan_result.viruses:
                print("- {} ({})".format(virus.name, virus.type))
        elif scan_result.status == scanner.SCAN_RESULT_ERROR:
            print("An error occurred during scanning.")
    except errors.ScanError as e:
        print("An error occurred during scanning: {}".format(str(e)))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <file_path>".format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print("File not found.")
        sys.exit(1)

    print("Scanning file {}...".format(file_path))
    start_time = time.time()
    scan_file(file_path)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time: {:.2f} seconds".format(elapsed_time))
