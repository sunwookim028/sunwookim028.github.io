.PHONY: help setup serve cv clean

help:
	@echo "Targets:"
	@echo "  make setup     reproduce from scratch: bundler install into vendor/ (see README for Ruby prereq)"
	@echo "  make serve     live-reload Jekyll on http://127.0.0.1:4000"
	@echo "  make cv        build cv.pdf from cv/cv.tex"
	@echo "  make clean     remove CV build artifacts and stray Jekyll output"

setup:
	bundle config set --local path vendor/bundle
	bundle install

serve:
	pkill -f jekyll; bundle exec jekyll serve --livereload

cv:
	$(MAKE) -C cv

clean:
	$(MAKE) -C cv clean
	rm -rf cv/_site
