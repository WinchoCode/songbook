"""Script to split a text file containing multiple hymns into individual LaTeX files."""
import os
import re

def sanitize_filename(title):
    """Replace invalid filename characters with underscore"""
    return re.sub(r'[\\/:*?"<>|]', '_', title)

# Input text file (all hymns together)
INPUT_FILE = "all_songs.txt"
# Output folder for songs
OUTPUT_FOLDER = "songs"

# Ensure the output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Split songs by marker (### Title)
blocks = content.strip().split("### ")
blocks = [b.strip() for b in blocks if b.strip()]  # remove empties

for block in blocks:
    lines = block.splitlines()
    song_title = lines[0].strip()
    LYRIC_LINES = [line.strip() for line in lines[1:]] # lyrics only
    
    formatted_lyrics = []
    for i, line in enumerate(LYRIC_LINES):
        if line == "":
            # Empty line → paragraph break
            formatted_lyrics.append("")
        else:
            # If next line is not empty, add \\
            if i + 1 < len(LYRIC_LINES) and LYRIC_LINES[i + 1] != "":
                formatted_lyrics.append(line + " \\\\")
            else:
                formatted_lyrics.append(line)
                
    lyrics = "\n".join(formatted_lyrics)

    # Create safe filename
    filename = sanitize_filename(song_title) + ".tex"
    filepath = os.path.join(OUTPUT_FOLDER, filename)

    # Wrap lyrics in LaTeX song environment
    TEX_CONTENT = f"""\\songtitle{{{song_title}}}
\\begin{{song}}
{lyrics}
\\end{{song}}
"""

    with open(filepath, "w", encoding="utf-8") as out:
        out.write(TEX_CONTENT)

    print(f"✅ Created {filepath}")
