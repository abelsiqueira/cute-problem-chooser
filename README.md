cute-problem-chooser
====================

Copyright 2014-2015 - Abel Soares Siqueira - abel.s.siqueira@gmail.com
Gpl v3.

Based on the CUTEr Problem Chooser.
Scripts to select specific CUTE(r|st) problems, using the description provided
in the website.

Contributors of the original project:

* Leandro Prudente - lfprudente@gmail.com
* Raniere Gaia Costa da Silva - r.gaia.cs@gmail.com
* Me - abel.s.siqueira@gmail.com

* * *
Overview
--------

In the beginning of 2015, the scripts were completely remade, because of two
things:

  - The classification of one problem in the site was wrong, which means more
    could be also.
  - It is possible to obtain all information obtained by the C program using
    only the sifdecoder (In both situations, CUTEst need(ed) to be installed.)

Currently, the program consist of scripts to run sifdecoder to all problems and
select problem according to (hardcoded) criterions.

The expected changes are

  - make this a package and create executable files using this package;
  - make it work with a command line interface;
  - create a graphic interface, if someone accepts the job;
  - make this compatible with Python 2, if possible.

* * *
Installing and Running
----------------------

You need python 3 to run the scripts, which is the version expected by the
command `python`.

No installation is required, and unless the sif problems were updated since

    2015, January, 16th

there is no need to update the sif.json list. Otherwise, you need to install
CUTEst (only sifdecoder is needed), and run

    $ ./src/gen-json.py > sif.json

To select the problems according to your criteria, you have to open the file
`select-cute-problems.py`, modify it, and then run
    
    $ ./select-cute-problems.py

The list will be printed on the default output and can redirect it as you wish.
This is obviously bad, and will be changed.

* * *
License
-------

This software is available under the GNU Public License v.3,
which can be seen in COPYING.
Unless otherwise noted, all source is under this license.
