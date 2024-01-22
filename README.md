# GA runner demo

This is a demo repository to help show how you might set up your own runners for Github Actions. 

A useful trick with runners: if you run your CI in Docker containers ... you _really_ cache a 
whole bunch of stuff! No need to wait until Python install/downloads stuff, you can test right 
away! So for some jobs ... runners aren't just cheaper, they faster! 

It's potentially especially cool if you run on something like [leaf.cloud](https://www.leaf.cloud/)
which offers carbon negative computing.
