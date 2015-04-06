# PyCon 2015 Scikit-learn Tutorial

*Instructor: Jake VanderPlas*

- email: <jakevdp@uw.edu>
- twitter: [@jakevdp](https://twitter.com/jakevdp)
- github: [jakevdp](http://github.com/jakevdp)

This repository will contain files and other info associated with my PyCon
2015 scikit-learn tutorial.

## Installation Notes
This tutorial requires the following packages:

- Python version 2.6-2.7 or 3.3-3.4
- `numpy` version 1.5 or later: http://www.numpy.org/
- `scipy` version 0.10 or later: http://www.scipy.org/
- `matplotlib` version 1.3 or later: http://matplotlib.org/
- `scikit-learn` version 0.14 or later: http://scikit-learn.org
- `ipython` version 2.0 or later, with notebook support: http://ipython.org

The easiest way to get these is to use the [conda](https://store.continuum.io/) environment manager.
I suggest downloading and installing [miniconda](conda.pydata.org/miniconda.html).

Once this is installed, the following command will install all required packages in your Python environment:
```
$ conda install numpy scipy matplotlib scikit-learn ipython-notebook
```

Alternatively, you can download and install the (very large) Anaconda software distribution, found at https://store.continuum.io/.

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