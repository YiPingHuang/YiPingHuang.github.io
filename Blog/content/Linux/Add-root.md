Title: Add super user account in Ubuntu
Slug: Root Ubuntu
Date: 2014/06/23
Tags: Ubuntu-14.04,Linux
Summary: Use su as usuall

Sometimes sudo might be hard to understand for me... su is an easier way for me
to understand what I am doing...

>sudo passwd root

Then, su is ready for using.

I encounter this problem since I don't know where to set the variables for root.
And using sudo is always confusing since its .bashrc file is obviously not the
one for the user. When I try to build openmpi library by intel compiler, sudo
cannot use the right variables. In order to install it under /opt with the right
permission, setting up a su account is the most easy way that came to my mind...
