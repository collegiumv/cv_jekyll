#!/bin/sh

for file in `find . -name "*.md"`; do
    echo "$file"; emacs --batch "$file" \
        --eval '(setq-default indent-tabs-mode nil)' \
        --eval '(whitespace-cleanup)' \
        -f 'save-buffer'
done
