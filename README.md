# Christian Songbook (LaTeX + Python)

## Workflow
1. Write songs in `all_songs.txt` with `### Title` markers.
2. Run `python split_all_songs.py` → creates `songs/*.tex`.
3. Run `python sort_songs_alphabetically.py` → creates `songs_sorted.tex`.
4. Compile with `latexmk -xelatex main.tex` → `main.pdf`.

## Optional Workflow
1. Create a folder called "songs"
2. In that folder, create individual files for each song using the song_template.tex as example.
3. Run `python sort_songs_alphabetically.py` → creates `songs_sorted.tex`.
4. Compile with `latexmk -xelatex main.tex` → `main.pdf`.

## GUI Option
Run `python songbook_gui.py` to add/edit songs and generate PDF without touching LaTeX directly. -- This is still not in place, it doesn´t work

## Install packages
pip install -r requirements.txt

### For Latex packages:
1. Download TeX Live installer: https://tug.org/texlive/acquire-netinstall.html
2. Run installer → choose Full scheme (ensures all packages included).
3. By default, it installs to C:\texlive\2025\bin\windows. Be sure to add the path to the Environment Variables -> user variables -> path