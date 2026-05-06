log_file = "app.log"

error_count = 0

with open(log_file, 'r') as file:
    if "ERROR" in file:
        print(line.strip())
        error_count +=1

print(f"\nTotal error: {error_count}")