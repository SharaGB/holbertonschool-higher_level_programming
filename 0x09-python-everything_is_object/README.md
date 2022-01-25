# Python - Everything is object

<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg" alt="" style="">

<h2>Background Context</h2>
<p>Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.</p>

<p>BTW, have you ever modified a variable without knowing it or wanting to? I mean:</p>

<pre><code>&gt;&gt;&gt; a = 1
&gt;&gt;&gt; b = a
&gt;&gt;&gt; a = 2
&gt;&gt;&gt; b
1
&gt;&gt;&gt; 
</code></pre>

<p>OK. But what about this?</p>

<pre><code>&gt;&gt;&gt; l = [1, 2, 3]
&gt;&gt;&gt; m = l
&gt;&gt;&gt; l[0] = 'x'
&gt;&gt;&gt; m
['x', 2, 3]
&gt;&gt;&gt; 
</code></pre>

<p><img src="https://media.giphy.com/media/wAjfQ9MLUfFjq/giphy.gif" alt="" style=""><br>
<br></p>

<p>This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. 
You should <strong>read all documentation first (as usual :))</strong>, then take the time to <strong>think and brainstorm with your peers</strong> about what you think and why. <strong>Try to do this without coding anything for a few hours</strong>.</p>

<p>Trying examples in the Python interpreter will give you most of the answers without having to think about it. <strong>Don’t go this route</strong>. First read, then think, then brainstorm together. Only then you can test in the interpreter.</p>

<p>It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.
The biggest mandatory task is the blog post and it will count for 50% of the total score of the project.</p>

<p>Note that during interviews for Python positions, <strong>you will most likely have to answer to these type of questions</strong>.</p>

<p>All your answers should be only one line in a file. No space before or after the answer.</p>

<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a href="/rltoken/n1x09X-KJSllpJkJorBw2A" title="9.10. Objects and values" target="_blank">9.10. Objects and values</a> </li>
<li><a href="/rltoken/3teQMNNfDeyGvCtZfjsf5g" title="9.11. Aliasing" target="_blank">9.11. Aliasing</a> </li>
<li><a href="/rltoken/JuPVygeoG27Q_qKxB2lP8g" title="Immutable vs mutable types" target="_blank">Immutable vs mutable types</a> </li>
<li><a href="/rltoken/UbL96sV3cIxewdQPW_zwRw" title="Mutation" target="_blank">Mutation</a> (<em>Only this chapter</em>)</li>
<li><a href="/rltoken/-t_1VsmKlgWHszL5y1YiKA" title="9.12. Cloning lists" target="_blank">9.12. Cloning lists</a> </li>
<li><a href="/rltoken/IdBAdTYNLuS3YpRRQIam6Q" title="Python tuples: immutable but potentially changing" target="_blank">Python tuples: immutable but potentially changing</a> </li>
</ul>

<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a href="/rltoken/d0Wvl9mlCY4CQDJg1qzamQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>
<ul>
<li>Why Python programming is awesome</li>
<li>What is an object</li>
<li>What is the difference between a class and an object or instance</li>
<li>What is the difference between immutable object and mutable object</li>
<li>What is a reference</li>
<li>What is an assignment</li>
<li>What is an alias</li>
<li>How to know if two variables are identical</li>
<li>How to know if two variables are linked to the same object</li>
<li>How to display the variable identifier (which is the memory address in the CPython implementation)</li>
<li>What is mutable and immutable</li>
<li>What are the built-in mutable types</li>
<li>What are the built-in immutable types</li>
<li>How does Python pass variables to functions</li>
</ul>

<h2>Requirements</h2>
<h3>Python Scripts</h3>
<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h3><code>.txt</code> Answer Files</h3>
<ul>
<li>Only one line</li>
<li>No Shebang</li>
<li>All your files should end with a new line</li>
</ul>
