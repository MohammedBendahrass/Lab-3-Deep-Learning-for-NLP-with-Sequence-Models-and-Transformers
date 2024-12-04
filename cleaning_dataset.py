import re

def clean_text(file_path, output_file):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    cleaned_lines = []
    for line in lines:
        # Remove navigation and filler text
        if re.search(r"(تخطي|اضغط هنا|إذهب|اعرض المزيد|البث الحي|محتوى رئيسي)", line):
            continue
        
        # Remove short or repetitive lines
        if len(line.strip()) < 10 or line.strip() in cleaned_lines:
            continue
        
        # Normalize Arabic characters
        normalized_line = re.sub(r"[إأآا]", "ا", line)
        normalized_line = re.sub(r"ى", "ي", normalized_line)
        normalized_line = re.sub(r"ة", "ه", normalized_line)
        cleaned_lines.append(normalized_line.strip())

    # Save cleaned data
    with open(output_file, "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(cleaned_lines))
    print(f"Cleaned data saved to {output_file}")

# Clean both datasets
clean_text("bbc.txt", "bbc_cleaned.txt")