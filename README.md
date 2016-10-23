Unbackslash
===========

Instead of creating the expected directory structure, `unzip(1)`
baked the entire path into the file names. I think this was because the source
contained backslash and forward-slash separated paths. So I wrote this script
to find files with backslashes in their names, replace them for slashes and
create the missing dir tree. 

I only used this once so use with extreme caution, at your own risk, and 
make a backup first.

License
=======

WTFPL with one additional clause:

 1. Don't blame me.

