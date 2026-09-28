#!/bin/bash

SOURCE="/home/stas/Documents/Obsidian Vault/Inżynierowie Przyszłości/"
DEST="/home/stas/Documents/WAVE/"

rsync -av --filter=':- .gitignore' "$SOURCE" "$DEST"
