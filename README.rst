nibelis-dl
==========

nibelis-dl is a command-line tool to download pay slips from Nibelis website.


Installation
------------

To install::

  pip install nibelis-dl

Or simply download it, it's a single-file script::

  https://github.com/benoitryder/nibelis-dl/raw/master/nibelis_dl.py


Use
---

Just run::

  nibelis-dl

It will prompt for username and password, then download pay slips from Nibelis'
website, starting from the earliest one.
Already download files will not be downloaded again.

Output directory and filename format can be configured using command line
options.

