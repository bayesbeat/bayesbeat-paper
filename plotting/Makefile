# Makefile to run notebooks and zip all PDFs from nested figures/ directories flatly

# Find all notebooks
NOTEBOOKS := $(wildcard *.ipynb)
MARKERS := $(NOTEBOOKS:.ipynb=.run)

# Default target
all: $(MARKERS)

# Run each notebook and create marker file
%.run: %.ipynb
	jupyter nbconvert --to notebook --execute --inplace $< && touch $@


# Recursively find PDFs under figures/
FIGURES := $(shell find -L figures -type f -name '*.pdf' ! -path '*/.ipynb_checkpoints/*')

# Zip them flat (no directory structure preserved)
figures.zip: $(FIGURES)
	zip -j figures.zip $(FIGURES)

# Clean intermediate files
clean:
	rm -f *.run figures.zip
