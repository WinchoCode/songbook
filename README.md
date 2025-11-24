# Christian Songbook (LaTeX + Python)

## Workflow
1. Write songs in `all_songs.txt` with `### Title` markers.
2. Run `python split_all_songs.py` → creates `songs/*.tex`.
3. Run `python build_songbook.py` → creates `songs_sorted.tex`.
4. Compile with `latexmk -xelatex main.tex` → `main.pdf`.

## Optional Workflow
1. Create a folder called "songs"
2. In that folder, create individual files for each song using the song_template.tex as example.
3. Run `python build_songbook.py` → creates `songs_sorted.tex`.
4. Compile with `latexmk -xelatex main.tex` → `main.pdf`.

## GUI Option
Run `python songbook_gui.py` to add/edit songs and generate PDF without touching LaTeX directly. -- This is still not in place, it doesn´t work

# Install packages
pip install -r requirements.txt