.PHONY: preview clean

PORT ?= 4000

# Repo is mounted read-only; gems are cached in .preview/ so restarts are fast.
# Note: the /kcc-ride/ redirect stubs point at 0.0.0.0 in preview; jekyll serve rewrites site.url.
preview:
	mkdir -p .preview
	docker run --rm --init -p 127.0.0.1:$(PORT):4000 \
	  -v "$(CURDIR)":/src:ro -v "$(CURDIR)/.preview":/cache \
	  -e BUNDLE_PATH=/cache/gems -e BUNDLE_APP_CONFIG=/cache -e BUNDLE_GEMFILE=/cache/Gemfile \
	  alpine sh -c 'apk add -q ruby-full ruby-dev build-base openssl-dev && cp /src/Gemfile /cache/ && cd /src && \
	    bundle install --quiet && chmod -R a+rwX /cache && \
	    bundle exec jekyll serve --host 0.0.0.0 --watch --force_polling -d /tmp/_site'

clean:
	rm -rf _site .sass-cache .preview
