# This is resume-sfllaw's Makefile, used to generate curriculum vitae.
# Copyright (C) 2002,2003  Simon Law
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

# Part of resume-sfllaw, version 1.3.
#
# This Makefile generates resumes derived from resume-sfllaw.tex into
# various formats.  It outputs TeX's DVI format, Adobe PostScript and
# PDF, and also XHTML 1.0 Transitional.  It can also copy or upload
# your resume (and this makefile) to your website, so you can show it
# off to the world.
#
# In order to generate resumes using this package, you will need the
# following programs installed:
#
# - GNU Make
# - TeX (including LaTeX and pdfTeX)
#
# You may also wish to get:
#
# - GhostScript
# - TeX4ht
# - SSH
# - GNU tar
#
# It is quite simple to generate a resume if you know LaTeX.  To
# generate resume-sfllaw.tex in various formats:
#
# make resume-sfllaw.dvi
#	generates a resume in TeX's DeVice Independent (DVI) format.
#
# make resume-sfllaw.pdf
#	generates a resume in Adobe's Portable Document Format (PDF).
#
# make resume-sfllaw.ps
#	generates a resume in Adobe's PostScript format (PS).
#
# make resume-sfllaw.html
#	generates a resume in XHTML 1.0 Transitional format with CSS.

## Edit the following options to match your setup. ###################

# Default rules:
#
# make
#	generates all RESUMES in all FORMATS specified.
#
# make cleanauxs
#	removes all temporary generated files.
#
# make clean
#	removes all generated files.
#
# List the RESUMES you wish to generate, omitting the .tex extension.
# Specify more than one resume by separating filenames with a space.
RESUMES = resume-sfllaw
# The FORMATS to generate, and also the ones to upload.
FORMATS = html css dvi pdf ps

# Copying files to a local directory:
#
# make cp
#	copies your RESUMES in the FORMATS to LOCAL_DIR.
#
LOCAL_DIR = ~/public_html/narcissism/

# Uploading files to a remote SERVER and puts them in the REMOTE_DIR
# directory:
#
# make scp
#	copies your RESUMES in the FORMATS over SCP.
#
# make star
#	copies your RESUMES in the FORMATS over SSH using GNU tar.
#
SERVER = sfllaw.ca
REMOTE_DIR = public_html/narcissism/

######################################################################

# Ensure that we are using a decent Make.
ifndef MAKE
$(error This makefile requires GNU Make)
else
ifeq (,$(findstring GNU Make,$(shell $(MAKE) --version)))
$(error This makefile requires GNU Make)
endif
endif

# Define the programs and the parameters used to generate the resume.
LATEX = pdflatex
LATEX2DVI = $(LATEX) \\pdfoutput=0 \\input
LATEX2PDF = $(LATEX) \\pdfoutput=1 \\input
LATEX2HTML = sh -e htlatex '$(1)' '$(basename $(1)).cfg' ' -cunihtf -utf8'
PDF2PS = pdf2ps

# Expand the formats and resumes so that the 'all' target can build them.
ALL_FORMATS = $(foreach format,$(FORMATS),\
		$(foreach resume,$(RESUMES),$(resume).$(format)))

# Expand all the sources
ALL_RESUMES = $(foreach resume,$(RESUMES),$(resume).tex)

# Also note which suffixes are auxillary and should be cleaned up.
HTML_AUXS = 4ct 4tc cfg idv lg tmp xref html css
TEX_AUXS = 4cs 4pp aux log dvi pdf tex
ALL_HTML_AUXS = $(foreach aux,$(HTML_AUXS) $(TEX_AUXS),\
		  $(foreach resume,$(RESUMES),_html.$(resume).$(aux)))
ALL_TEX_AUXS = $(foreach fmt,dvi pdf,$(foreach aux,$(TEX_AUXS),\
		 $(foreach resume,$(RESUMES),_$(fmt).$(resume).$(aux))))
ALL_AUXS = $(ALL_HTML_AUXS) $(ALL_TEX_AUXS)

.PHONY : all cp scp star clean cleanauxs FORCE

all : $(ALL_FORMATS)

cp : all
	cp -f $(ALL_RESUMES) $(ALL_FORMATS) $(MAKEFILE_LIST) \
		'$(wildcard $(LOCAL_DIR)/)'

star : all
	tar cf - -- $(ALL_RESUMES) $(ALL_FORMATS) $(MAKEFILE_LIST)\
		| ssh -C '$(SERVER)' tar xf - -C '$(REMOTE_DIR)'

scp : all
	scp -C $(ALL_RESUMES) $(ALL_FORMATS) $(MAKEFILE_LIST) \
		'$(SERVER):$(REMOTE_DIR)'

clean : cleanauxs
	rm -f $(ALL_FORMATS)

cleanauxs :
	rm -f $(ALL_AUXS)

# Generate the DVI file under the _dvi prefix and link it back to the
# desired one.
%.dvi : %.tex $(MAKEFILE_LIST)
	ln -f '$<' '_dvi.$<'
	$(LATEX2DVI) '_dvi.$<'
	ln -f '_dvi.$@' '$@'

# Generate the PDF file under the _pdf prefix and link it back to the
# desired one.
%.pdf : %.tex $(MAKEFILE_LIST)
	ln -f '$<' '_pdf.$<'
	$(LATEX2PDF) '_pdf.$<'
	ln -f '_pdf.$@' '$@'

# Generate the PS file, using the PDF file.
%.ps : %.pdf $(MAKEFILE_LIST)
	$(PDF2PS) '$<' '$@'

# Generate the XHTML file under the _html prefix and link it back to
# the desired one.
%.html : %.tex $(MAKEFILE_LIST)
	ln -f '$<' '_html.$<'
	rm -f '_html.$*.4cs' '_html.$*.4pp' '_html.$*.cfg'
	$(LATEX2DVI) '_html.$<'
	$(call LATEX2HTML,_html.$<)
	$(SHELL) '_html.$*.4pp' '_html.$*' '_html.$<' '_html.$@'
	ln -f '_html.$@' '$@'

# Generate the CSS file, which is auto-magically created with the XHTML.
%.css : %.html ;
	ln -f '_html.$@' '$@'

# Empty .tex rule, so nothing is generated for TeX source files.
%.tex : ;

# Empty MAKEFILE_LIST rule, so nothing is generated for Makefiles.
$(MAKEFILE_LIST) : ;
