Apache Rewrite Maps (Python)
==========================
A set of rewrite maps for Apache written in Python to extend the functionality of mod_rewrite and/or .htaccess files.
You'll be able to convert underscores to spaces, underscores to hyphens, or spaces to hyphens. 

# Requirements
- Python 2.7 
- Apache with mod_rewrite enabled

# Installation

1. Download under2space.py, under2hyphen.py , and/or space2hyphen.py to a secure directory (one that is only accessible to apache) ,
2. Give execution permissions to these scripts with:
	```
	cd /path/to/secure/directory/
	sudo chmod +x *.py
 	```
3. Add the following RewriteMap conditions to your Virtual Host file. You can use the following as an example:

	```
	<VirtualHost *:80>
		RewriteEngine On
		
		RewriteMap under2space prg:/path/to/under2space.py
		RewriteMap under2hyphen prg:/path/to/under2hyphen.py
		RewriteMap space2hyphen	prg:/path/to/space2hyphen.py
	   
		# Sample usage
		RewriteRule ^(.*).php $ /blog/${under2space:$1} [L,R=301]    
		RewriteRule ^(.*).py $ /articles/${under2hyphen:$1} [L,R=301]    
		RewriteRule ^(.*).asp $ /api/${space2hyphen:$1} [L,R=301]    
	</VirtualHost>
	```
4. Restart Apache.


### Notes
It is very important to keep in mind that these scripts will be loaded only once by Apache, and they will keep running all the time. 
So if you plan to modify any of this scripts live , you'll need to restart apache every time.
For debugging purposes, I strongly recommend you adding the following to your virtual host:
```
        RewriteEngine On
        RewriteLogLevel 9
        RewriteLog /var/log/apache2/rewrite.log
```



 
