log_file = "app.log"
output_file = "errors.log"

error_lines = []

# Read and collect errors
with open(log_file, 'r') as file:
    for line in file:
        if "ERROR" in line:
            clean_line = line.strip()
            error_lines.append(clean_line)


# Print errors
print("\n".join(error_lines))
print(f"\nTotal errors: {len(error_lines)}")

# Save errors to file
with open(output_file, "w") as out_file:
    for error in error_lines:
        out_file.write(error + "\n")

print(f"\nErrors saved to {output_file}")
