# JavaScript - Web Scraping
<div class="well clean" id="project-description">
  <h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON" title="Working with JSON data" target="_blank">Working with JSON data</a> </li>
<li><a href="https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319" title="The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco" target="_blank">The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco</a> </li>
<li><a href="https://github.com/request/request" title="request module" target="_blank">request module</a> </li>
<li><a href="https://github.com/mbeaudru/modern-js-cheatsheet" title="Modern JS" target="_blank">Modern JS</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="https://fs.blog/feynman-learning-technique/" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why JavaScript programming is amazing</li>
<li>How to manipulate JSON data</li>
<li>How to use <code>request</code> and fetch API</li>
<li>How to read and write a file using <code>fs</code> module</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS using <code>node</code> (version 10.14.x)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/node</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be <code>semistandard</code> compliant. <a href="https://standardjs.com/rules.html" title="Rules of Standard" target="_blank">Rules of Standard</a> + <a href="https://github.com/standard/semistandard" title="semicolons on top" target="_blank">semicolons on top</a>. Also as reference: <a href="https://github.com/airbnb/javascript" title="AirBnB style" target="_blank">AirBnB style</a></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<h2>More Info</h2>

<h3>Install Node 10</h3>

<pre><code>$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</code></pre>

<h3>Install semi-standard</h3>

<p><a href="https://github.com/standard/semistandard" title="Documentation" target="_blank">Documentation</a></p>

<pre><code>$ sudo npm install semistandard --global
</code></pre>

<h3>Install <code>request</code> module and use it</h3>

<p><a href="https://github.com/axios/axios" title="Documentation" target="_blank">Documentation</a></p>

<pre><code>$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
</code></pre>

<p><strong>Notes:</strong> Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).</p>

</div>
