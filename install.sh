#!/bin/bash
set -e

FILE_BASENAME="linux_madness"
SOURCE_DIR="$(cd "$(dirname "$0")" && pwd)"
FORTUNE_TXT="$SOURCE_DIR/$FILE_BASENAME"
FORTUNE_DAT="$SOURCE_DIR/$FILE_BASENAME.dat"

if [ "$(id -u)" -eq 0 ]; then
    INSTALL_PATH="/usr/share/games/fortunes"
else
    INSTALL_PATH="$HOME/.fortunes"
    mkdir -p "$INSTALL_PATH"
fi

echo "Installing to $INSTALL_PATH"
strfile "$FORTUNE_TXT"
cp "$FORTUNE_TXT" "$FORTUNE_DAT" "$INSTALL_PATH"
echo "Done. Try with: fortune $FILE_BASENAME"
