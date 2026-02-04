"""Script to sort individual LaTeX song files alphabetically by title, renumber them,
 and combine into a single LaTeX file with two-column layout."""
import os
import re

# Folder where all individual .tex songs are stored
SONGS_FOLDER = "songs"
# Output file that contains all songs in alphabetical order
OUTPUT_FILE = "songs_sorted.tex"

# Collect all .tex song files
song_files = [f for f in os.listdir(SONGS_FOLDER) if f.endswith(".tex")]

songs = []
for filename in song_files:
    filepath = os.path.join(SONGS_FOLDER, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract the title from \songtitle{...}
    match = re.search(r"\\songtitle\{(.+?)\}", content)
    if match:
        title = match.group(1).strip()
        songs.append((title, filename, content))
    else:
        print(f"⚠️ Warning: No title found in {filename}")

# Sort songs alphabetically by title
songs_sorted = sorted(songs, key=lambda x: x[0].lower())

# Build LaTeX body with renumbered titles
renumbered_blocks = []
for i, (title, filename, content) in enumerate(songs_sorted, start=1):
    # Replace the title with "N. Title"
    new_content = re.sub(
        r"\\songtitle\{.+?\}",
        f"\\\\songtitle{{{i}. {title}}}",
        content,
        count=1
    )

    # Clean up extra whitespaces
    new_content = new_content.strip()

    # Add commands to prevent page/column breaks within songs
    wrapped_content = f"\\par\\nonpagebreak[4]\n{new_content}\n\\par"
    renumbered_blocks.append(wrapped_content)

# Write to output file
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("% Auto-generated file, do not edit manually\n\n")
    f.write("\\begin{multicols}{2}\n")
    f.write("\n\n".join(renumbered_blocks))
    f.write("\n\\end{multicols}\n")

print(f"✅ Alphabetical songbook with numbering written to {OUTPUT_FILE}")
print(f"✅ Total songs: {len(songs_sorted)}")
