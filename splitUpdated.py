import os

# Input text file (all hymns together)
input_file = "all_songs.txt"
# Output folder for songs
output_folder = "songs"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# Split songs by marker (### Title)
blocks = content.strip().split("### ")
blocks = [b.strip() for b in blocks if b.strip()]  # remove empties

for block in blocks:
    lines = block.splitlines()
    title = lines[0].strip()
    lyrics_lines = [line.strip() for line in lines[1:]]  # lyrics only

    formatted_lyrics = []
    for i, line in enumerate(lyrics_lines):
        if line == "":  
            # Empty line → paragraph break
            formatted_lyrics.append("")
        else:
            # If next line is not empty, add \\
            if i + 1 < len(lyrics_lines) and lyrics_lines[i+1] != "":
                formatted_lyrics.append(line + " \\\\")
            else:
                formatted_lyrics.append(line)

    lyrics = "\n".join(formatted_lyrics)

    # Create safe filename
    filename = title.replace(" ", "_").replace("/", "-") + ".tex"
    filepath = os.path.join(output_folder, filename)

    # Wrap lyrics in LaTeX song environment
    tex_content = f"""\\songtitle{{{title}}}
\\begin{{song}}
{lyrics}
\\end{{song}}
"""

    with open(filepath, "w", encoding="utf-8") as out:
        out.write(tex_content)

    print(f"✅ Created {filepath}")
