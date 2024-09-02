import sys
import signal

# Initialize metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    """Print the current statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def handle_interrupt(signal, frame):
    """Handle keyboard interruption to print statistics."""
    print_statistics()
    sys.exit(0)

# Register signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        
        # Validate line format
        if len(parts) < 7:
            continue
        
        ip_address = parts[0]
        date = parts[3] + " " + parts[4]
        request = parts[5] + " " + parts[6] + " " + parts[7]
        status_code = parts[8]
        file_size = parts[9]

        # Check for valid status code and file size
        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        # Update metrics
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except Exception as e:
    print(f"Error: {e}")

# Final statistics print in case of an EOF
print_statistics()
