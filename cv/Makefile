# Makefile for building CV PDF
# Target location in repo: /cv/Makefile
# Usage:
#   make          build cv.pdf
#   make watch    continuous rebuild on edit (requires latexmk -pvc support)
#   make clean    remove build artifacts

.PHONY: all watch clean

all: ../cv.pdf

../cv.pdf: cv.tex
	latexmk -pdf -interaction=nonstopmode -halt-on-error cv.tex
	mv cv.pdf ../

watch: cv.tex
	latexmk -pdf -pvc -interaction=nonstopmode cv.tex

clean:
	latexmk -C
	rm -f *.aux *.log *.out *.fdb_latexmk *.fls *.synctex.gz
