# This is a Makefile, used to generate web-of-trust graphs for GnuPG keyrings
# Copyright (C) 2004  Simon Law
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

# This Makefile generates graphs of GnuPG keyrings.  It outputs
# PNG images of these graphs.
#
# In order to generate graphs using this package, you will need the
# following programs installed:
#
# - GNU Make
# - Sig2Dot
# - Springgraph
# - pngcrush
#
# You will want to put the hexadecimal key-IDs in a file named
# 'small.keys'.  These will be the keys plotted in your graph, which
# comes out as 'small.ps' and 'small.png'.
#
# You can also generate a 'large.ps' file containing your signatories'
# signatories.  This takes the keys listed in 'small.keys' and
# generates a 'large.keys' containing more keys.

# These are the required programs used to generate diagrams
GPG = gpg --no-default-keyring --keyring './$(1)' --keyserver pgpkeys.mit.edu
SIG2DOT = sig2dot
SPRINGGRAPH = springgraph -s 2

# Here are optional programs, provided by GraphViz and ImageMagick.
# They make for more attractive graphs, however GraphViz is non-free.
# You can use them by passing NONFREE=1 into the Makefile.
NEATO = neato -Goverlap=false -Gsep.1 -Gsplines=true -Tps
CONVERT = convert
PNGCRUSH = pngcrush -m 7

all : small.ps small.png

ifdef NONFREE

%.png : %.ps
	$(CONVERT) '$<' 'tmp_$@'
	$(PNGCRUSH) 'tmp_$@' '$@'
	rm -f 'tmp_$@'

%.ps : %.dot
	$(NEATO) '$<' > '$@'

else

%.png : %.dot
	$(SPRINGGRAPH) < '$<' > 'tmp_$@'
	$(PNGCRUSH) 'tmp_$@' '$@'
	rm -f 'tmp_$@'

%.ps : %.png
	convert '$<' '$@'

endif

%.dot : %.gpg
	$(call GPG,$<) --list-sigs `cat '$*.keys'`\
	  | $(SIG2DOT) -s '$*.html' > '$@'

%.html : %.dot

fetch : $(KEYS)
	-if [ -n '$(KEYRING)' -a -n '$(KEYS)' ]; then\
	  xargs $(call GPG,$(KEYRING)) --recv-keys < '$(KEYS)'; fi

small.keys : ;

large.keys : small.keys
	$(MAKE) 'KEYRING=large.gpg' 'KEYS=small.keys' fetch
	$(call GPG,large.gpg) --list-sigs `cat small.keys`\
	  | grep '^sig ' | cut -c 13-20 | sort | uniq -i > '$@.tmp'
	cat 'small.keys' '$@.tmp' | sort | uniq -i > '$@'
	rm -f '$@.tmp'

%.gpg : %.keys
	rm -f '$@'
	$(MAKE) 'KEYRING=$*.gpg' 'KEYS=$<' fetch

.PHONY : all fetch

.PRECIOUS : %.gpg %.dot
