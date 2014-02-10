#!/usr/bin/python -u

"""
This script replaces spaces with hypens

Project: https://github.com/LagrangianPoint/Apache-Rewrite-Maps-Python/

http://httpd.apache.org/docs/current/rewrite/rewritemap.html
http://fragmentsofcode.wordpress.com/2009/02/04/python-script-for-apache-rewritemap/
http://codeblow.com/questions/apache2-rewritemap-python-when-coming-back-null-apache-dangles/

HINTS FOR DEBUGGING:
        RewriteEngine On
        RewriteLogLevel 9
        RewriteLog /var/log/apache2/rewrite.log

"""

import sys

while sys.stdin:
	try:
		strLine = sys.stdin.readline().strip()   ## It is very important to use strip!
		strLine = strLine.replace(' ', '-')
		print strLine
		sys.stdout.flush()
	except:
		print "NULL"
		sys.stdout.flush()

