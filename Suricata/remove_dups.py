def remove_duplicates(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    seen = set()  # Store unique lines up until "sid:"
    unique_lines = []  # Store unique lines
    duplicates_removed = 0  # Counter for duplicates

    for line in lines:
        sid_index = line.find("sid:")  # Find index of "sid:"
        if sid_index != -1:  # If "sid:" found in line
            line_before_sid = line[:sid_index]  # Extract part of line before "sid:"
            if line_before_sid not in seen:  # If this part hasn't been seen before
                seen.add(line_before_sid)  # Add it to seen set
                unique_lines.append(line)  # And keep the line as unique
            else:
                duplicates_removed += 1  # If it has been seen, it's a duplicate
        else:
            unique_lines.append(line)  # If "sid:" not found in line, keep the line

    print(f'Number of duplicates removed: {duplicates_removed}')

    # Write the unique lines back to the file
    with open(file_name, 'w') as file:
        file.writelines(unique_lines)

remove_duplicates('suricata_rules.rules')
