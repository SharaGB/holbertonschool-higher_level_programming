#  Python - Hello, World

<div class="panel panel-default">
    <div class="panel-heading">
      <h3 class="panel-title">Concepts</h3>
    </div>
    <div class="panel-body">
      <p>
        <em>For this project, we expect you to look at these concepts:</em>
      </p>
      <ul>
          <li>
            <a href="https://intranet.hbtn.io/concepts/63">Python programming </a>
          </li>
          <li>
            <a href="https://intranet.hbtn.io/concepts/550">Python programming </a>
          </li>
          <li>
            <a href="https://intranet.hbtn.io/concepts/551">Python programming</a>
          </li>
      </ul>
    </div>
</div>

<div class="well clean" id="project-description">
  <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg" alt="" style=""></p>

<h2>Author’s disclaimer</h2>

<pre><code>Welcome to the Python world!

The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
If you've already played with Python, don't worry, fun things will come.
You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode. At Holberton, we won't start off with using PyCode, because it's much more strict compared to PEP8. Don't worry if you see a warning when you are running PEP8, you can ignore it.

Enjoy!

- Guillaume
</code></pre>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://docs.python.org/3/tutorial/index.html" title="The Python tutorial" target="_blank">The Python tutorial</a> (<em>only the first three chapters below</em>)</li>
<li><a href="https://docs.python.org/3/tutorial/appetite.html" title="Whetting Your Appetite" target="_blank">Whetting Your Appetite</a> </li>
<li><a href="https://docs.python.org/3/tutorial/interpreter.html" title="Using the Python Interpreter" target="_blank">Using the Python Interpreter</a> </li>
<li><a href="https://docs.python.org/3/tutorial/introduction.html" title="An Informal Introduction to Python" target="_blank">An Informal Introduction to Python</a> (<em>Read up until “3.1.2. Strings” included</em>)</li>
<li><a href="https://realpython.com/python-f-strings/" title="How To Use String Formatters in Python 3" target="_blank">How To Use String Formatters in Python 3</a> </li>
<li><a href="https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt" title="Learn to Program" target="_blank">Learn to Program</a> </li>
<li><a href="https://pypi.org/project/pycodestyle/" title="Pycodestyle -- Style Guide for Python Code" target="_blank">Pycodestyle – Style Guide for Python Code</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="https://fs.blog/feynman-learning-technique/" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why Python programming is awesome</li>
<li>Who created Python</li>
<li>Who is Guido van Rossum</li>
<li>Where does the name ‘Python’ come from</li>
<li>What is the Zen of Python</li>
<li>How to use the Python interpreter</li>
<li>How to print text and variables using <code>print</code></li>
<li>How to use strings</li>
<li>What are indexing and slicing in Python</li>
<li>What is the official Python coding style and how to check your code with <code>pycodestyle</code></li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file at the root of the repo, containing a description of the repository</li>
<li>A <code>README.md</code> file, at the root of the folder of <em>this</em> project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h3>Shell Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your scripts will be tested on Ubuntu 20.04 LTS</li>
<li>All your scripts should be exactly two lines long (<code>wc -l file</code> should print 2)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/bin/bash</code></li>
<li>All your files must be executable</li>
</ul>

<h3>C Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89</li>
<li>All your files should end with a new line</li>
<li>Your code should use the <code>Betty</code> style. It will be checked using <a href="https://github.com/holbertonschool/Betty/blob/master/betty-style.pl" title="betty-style.pl" target="_blank">betty-style.pl</a> and <a href="https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl" title="betty-doc.pl" target="_blank">betty-doc.pl</a></li>
<li>You are not allowed to use global variables</li>
<li>No more than 5 functions per file</li>
<li>In the following examples, the <code>main.c</code> files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own <code>main.c</code> files at compilation. Our <code>main.c</code> files might be different from the one shown in the examples</li>
<li>The prototypes of all your functions should be included in your header file called <code>lists.h</code></li>
<li>Don’t forget to push your header file</li>
<li>All your header files should be include guarded</li>
</ul>

<h2>More Info</h2>

<h3>Zen</h3>

<pre><code>The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
</code></pre>

<h3>Pycodestyle</h3>

<p><code>Pycodestyle</code> is now the <a href="https://github.com/PyCQA/pycodestyle/issues/466" title="new standard of Python style code" target="_blank">new standard of Python style code</a></p>

<p><br>
<br>
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/Flyingcircus_2.jpg" alt="" style=""></p>

</div>
