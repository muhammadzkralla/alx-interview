#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_file_size = 0
status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def print_stats():
    """ Print the statistics of file size and status codes """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """ Handle the keyboard interruption (CTRL + C) """
    print_stats()
    sys.exit(0)


# Set up signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()

        # Split the line based on spaces
        parts = line.split(" ")
        if len(parts) < 7:
            continue  # Skip if the format is not correct

        # Extract relevant fields
        try:
            ip_address = parts[0]
            date = parts[3][1:]
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update metrics
            total_file_size += file_size
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            continue  # Skip if there's an error

except KeyboardInterrupt:
    # Handle CTRL + C gracefully
    print_stats()
    sys.exit(0)

# Print final stats if the script ends naturally
print_stats()
