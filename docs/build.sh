#!/bin/bash
rm -rf _source _build _notebooks
mkdir -p _source/markdown
mkdir -p _source/notebooks

rsync -av --prune-empty-dirs --exclude 'docs/' --include='*/' --include='*.md' --exclude='*' ../ _source/markdown/
jupyter-book build .