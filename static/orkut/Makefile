# This is a Makefile, used to generate web-of-trust graphs for Orkut
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

# This Makefile generates graphs of Orkut friend networks.  It outputs
# PNG images of these graphs.
#
# In order to generate graphs using this package, you will need the
# following programs installed:
#
# - GNU Make
# - Orkut2Dot
# - Springgraph
# - pngcrush
#
# You will want to put the root Orkut user numbers in a file named
# 'graph.userid'.  These will be the keys plotted in your graph, which
# comes out as 'graph.ps' and 'graph.png'.  If you don't specify a
# 'graph.userid', then Orkut2Dot will pick the login account as the
# root user number.

# Orkut login information
USERNAME = sfllaw
PASSWORD =

# These are the required programs used to generate diagrams
ORKUT2DOT = ./orkut2dot
SPRINGGRAPH = springgraph -s 2

# Here are optional programs, provided by GraphViz and ImageMagick.
# They make for more attractive graphs, however GraphViz is non-free.
# You can use them by passing NONFREE=1 into the Makefile.
NEATO = neato -Goverlap=false -Gsep.1 -Gsplines=true -Tps
CONVERT = convert
PNGCRUSH = pngcrush -m 7

all : graph.ps graph.png

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

%.dot : %.userid
	$(ORKUT2DOT) '$(USERNAME)' '$(PASSWORD)' `cat $<` > '$@'

.PHONY : all

.PRECIOUS : %.dot
