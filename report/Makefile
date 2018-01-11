all: export
export:
	emacs --batch report.org --eval "(require 'org)" --eval "(load-file \"include/htmlize.el\")" --eval "(org-html-export-to-html)"
#publish:
#	scp report.html irc.vladg.net:/srv/www/s4ns_hhc/ && rsync -e ssh -avz images/ irc.vladg.net:/srv/www/s4ns_hhc/images/ && rsync -e ssh -avz js/ irc.vladg.net:/srv/www/s4ns_hhc/js/ && rsync -e ssh -avz css/ irc.vladg.net:/srv/www/s4ns_hhc/css/ && rsync -e ssh -avz fonts/ irc.vladg.net:/srv/www/s4ns_hhc/fonts/
