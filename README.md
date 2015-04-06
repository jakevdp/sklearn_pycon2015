# PyCon 2015 Scikit-learn Tutorial

*Instructor: Jake VanderPlas*

- email: <jakevdp@uw.edu>
- twitter: [@jakevdp](https://twitter.com/jakevdp)
- github: [jakevdp](http://github.com/jakevdp)

This repository will contain files and other info associated with my PyCon
2015 scikit-learn tutorial.

## Installation Notes
This tutorial will require recent installations of *numpy*, *scipy*,
*matplotlib*, *scikit-learn*, and *ipython* with ipython notebook.
The last one is important: you should be able to type

    ipython notebook

in your terminal window and see the notebook panel load in your web browser.
This tutorial is compatible with Python 2.6-2.7 and 3.3-3.4

For users who do not yet have these  packages installed, a relatively
painless way to install all the requirements is to use a package such as
[Anaconda CE](http://store.continuum.io/ "Anaconda CE"), which can be
downloaded and installed for free.

## Downloading the Tutorial Materials
I would highly recommend using git, not only for this tutorial, but for the
general betterment of your life.  Once git is installed, you can clone the
material in this tutorial by using the git address shown above:

    git clone git://github.com/jakevdp/sklearn_pycon2015.git

If you can't or don't want to install git, there is a link above to download
the contents of this repository as a zip file.  I may make minor changes to
the repository in the days before the tutorial, however, so cloning the
repository is a much better option.


## Notebook Listing
These notebooks in this repository can be statically viewed using the
excellent [nbviewer](http://nbviewer.ipython.org) site.  They will not
be able to be modified within nbviewer.  To modify them, first download
the tutorial repository, change to the notebooks directory, and type
``ipython notebook``.  You should see the list in the ipython notebook
launch page in your web browser.

To view the tutorial in nbviewer, follow [this link](http://nbviewer.ipython.org/urls/raw.github.com/jakevdp/sklearn_pycon2015/master/notebooks/Index.ipynb)

Note that some of the code in these notebooks will not work outside the
directory structure of this tutorial, so it is important to clone the full
repository if possible.