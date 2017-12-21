all: export publish
export:
	emacs --batch report.org --eval "(require 'org)" --eval "(load-file \"include/htmlize.el\")" --eval "(org-html-export-to-html)"
publish:
	scp report.html irc.vladg.net:/srv/www/s4ns_hhc/
