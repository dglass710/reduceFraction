# reduceFraction
A simple, self contained, command line tool that reduces fractions.
<br>
reduceFractionCLI.py is more aestetically pleasing in a terminal with color support however reduceFractionCLINoColor.py has less overhead. I wanted to make sure both are options as we all hate bloat-ware but having color is very helpful.  

Example I/O:

``` bash
user@computer:/path/to/current/directory> python3 reduceFractionCLI.py 16/24
16/24 = 2/3
user@computer:/path/to/current/directory> python3 reduceFractionCLI.py 16/32
16/32 = 1/2
user@computer:/path/to/current/directory> python3 reduceFractionCLI.py 24/32
24/32 = 3/4
user@computer:/path/to/current/directory> python3 reduceFractionCLI.py 88/100
88/100 = 22/25
```
