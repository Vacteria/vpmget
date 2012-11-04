#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
#  vpmget.py
#  
#  Copyright 2012 
#  * Miguel Angel Reynoso <miguel@vacteria.org>
#  * Daniel Angel gebaudo <dag@debian-ar.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# import modules
from sys import argv, exit
from getopt import getopt, error
from gettext import gettext
from gettext import textdomain
from gettext import bindtextdomain
from common import MainSettings
from install import InstallPackages
from remove import RemovePackages
from update import UpdateRepos

global progname
progname="vpmget"

# Native language support stuff
bindtextdomain(progname, "/usr/share/locale")
textdomain(progname)

#
# Main program function
#
def main(argv):
	shortOpts = "iruR:"
	longOpts  = ["install", "remove", "udate", "root="]
	
	try:
		opts, args = getopt(argv[1:], shortOpts , longOpts)
	except error, err :
		print err
		return 1

	s = MainSettings()
	
	for o, a in opts:
		if o in ("-i", "--install"):
			s.selector = "install"
		elif o in ("-r", "--remove"):
			s.selector = "remove"
		elif o in ("-u", "--update"):
			s.selector = "update"
		elif o in ("-R", "--root"):
			s.root = a

	if ( s.selector == "null" ):
		print(gettext("No main action was selected"))
		exit(1)
		
	switch = {
		"install":InstallPackages(s,args),
		"remove":RemovePackages(s,args),
		"update":UpdateRepos(s,args)
	}
		
if __name__ == '__main__':
	exit(main(argv))
