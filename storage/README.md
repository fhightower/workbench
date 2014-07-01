<p align="center"><img src="http://raw.github.com/supercowpowers/workbench/master/images/workbench.jpg"></p>
[![Build Status](https://travis-ci.org/SuperCowPowers/workbench.svg?branch=master)](https://travis-ci.org/SuperCowPowers/workbench)
[![Coverage Status](https://coveralls.io/repos/SuperCowPowers/workbench/badge.png)](https://coveralls.io/r/SuperCowPowers/workbench)
[![Code Health](https://landscape.io/github/SuperCowPowers/workbench/master/landscape.png)](https://landscape.io/github/SuperCowPowers/workbench/master)
[![Project Stats](https://www.ohloh.net/p/workbench/widgets/project_thin_badge.gif)](https://www.ohloh.net/p/workbench)

[![Stories](https://badge.waffle.io/supercowpowers/workbench.png?label=on_deck&title=On_Deck)](https://waffle.io/supercowpowers/workbench)
[![Stories](https://badge.waffle.io/supercowpowers/workbench.png?label=in_progress&title=In_Progress)](https://waffle.io/supercowpowers/workbench)
[![Gitter chat](https://badges.gitter.im/SuperCowPowers/workbench.png)](https://gitter.im/SuperCowPowers/workbench)

Workbench
=========
#### A medium-data framework for security research and development teams.
Workbench focuses on simplicity, transparency, and easy on-site customization. As an open source python project it provides light-weight task management, execution and pipelining for a loosely-coupled set of python classes. 

- **[Workbench Documentation](http://workbench.readthedocs.org/en/latest/)**
- [Users Email List](https://groups.google.com/forum/#!forum/workbench-users) (anyone can join)
- [Developers Email List](https://groups.google.com/forum/#!forum/workbench-devs) (anyone can join)

## Workbench Examples
* **<a href="http://nbviewer.ipython.org/url/raw.github.com/SuperCowPowers/workbench/master/notebooks/PCAP_to_Graph.ipynb">PCAP to Graph</a>** (A short teaser)
* **<a href="http://nbviewer.ipython.org/url/raw.github.com/SuperCowPowers/workbench/master/notebooks/Workbench_Demo.ipynb">Workbench Demo</a>**
* **<a href="http://nbviewer.ipython.org/url/raw.github.com/SuperCowPowers/workbench/master/notebooks/Adding_Worker.ipynb">Adding a new Worker</a>** (super hawt)
* **<a href="http://nbviewer.ipython.org/url/raw.github.com/SuperCowPowers/workbench/master/notebooks/PCAP_to_Dataframe.ipynb">PCAP to Dataframe</a>**
* **<a href="http://nbviewer.ipython.org/url/raw.github.com/SuperCowPowers/workbench/master/notebooks/PCAP_DriveBy.ipynb">PCAP DriveBy Analysis</a>**
* **<a href="http://nbviewer.ipython.org/url/raw.github.com/SuperCowPowers/workbench/master/notebooks/PE_SimGraph.ipynb">Using Neo4j for PE File Sim Graph</a>**
* **<a href="http://nbviewer.ipython.org/url/raw.github.com/SuperCowPowers/workbench/master/notebooks/Generator_Pipelines.ipynb">Generator Pipelines Notebook</a>**
* WIP Notebooks
	* **<a href="http://nbviewer.ipython.org/url/raw.github.com/SuperCowPowers/workbench/master/notebooks/Network_Stream.ipynb">Network Stream Analysis Notebook</a>**
	* **<a href="http://nbviewer.ipython.org/url/raw.github.com/SuperCowPowers/workbench/master/notebooks/PE_Static_Analysis.ipynb">PE File Static Analysis Notebook</a>**



<br>
<img src="http://raw.github.com/supercowpowers/workbench/master/images/warning.jpg" width=90 align="left">
### Pull the repository
<pre>
git clone https://github.com/supercowpowers/workbench.git
</pre>
**Warning!: The repository contains malcious data samples, be careful, exclude the workbench directory from AV, etc...**
<br><br>

## Installing Workbench:

### Workbench Client:
    $ pip install zerorpc; echo 'Done!'

### Workbench Server:
The indexers 'Neo4j' and 'ElasticSearch' are optional. We strongly suggest you install both of them but we also appreciate that there are cases where that's not possible or feasible.

#### Mac/OSX
- brew install mongodb
- brew install yara
- brew install libmagic
- brew install bro
   - Put the bro executable in your PATH (/usr/local/bin or wherever bro is)

#### Ubuntu (14.04 and 12.04)
- sudo apt-get install mongodb
- sudo apt-get install python-dev
- sudo apt-get install g++
- sudo apt-get install libssl0.9.8
- Bro IDS: 
   - Put the bro executable in your PATH (/opt/bro/bin or wherever bro is)

    In general the Bro debian package files are WAY too locked down with dependencies on exact versions of libc6 and python2.6. We have a more 'flexible' version [Bro-2.2-Linux-x86_64_flex.deb](https://s3-us-west-2.amazonaws.com/workbench-data/packages/Bro-2.2-Linux-x86_64_flex.deb). 
    - sudo dpkg -i Bro-2.2-Linux-x86_64_flex.deb
 
   If using the Debian package above doesn't work out:
   - Check out the Installation tutorial [here](https://www.digitalocean.com/community/articles/how-to-install-bro-ids-2-2-on-ubuntu-12-04)
   - or this one [here](http://www.justbeck.com/getting-started-with-bro-ids/)
   - or go to offical Bro Downloads [www.bro.org/download/](http://www.bro.org/download)

    
###Install Indexers:

#### Mac/OSX
- brew install elasticsearch
- pip install -U elasticsearch
- brew install neo4j
    - Note: You may need to install Java JDK 1.7 [Oracle JDK 1.7 DMG](http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jdk-7u51-macosx-x64.dmg) for macs.

#### Ubuntu (14.04 and 12.04)
- Neo4j: See official instructions for Neo4j [here](http://www.neo4j.org/download/linux)
    - Note: You may need to install Java JDK 1.7. If you have Java 1.7 installed , and error says otherwise, run update-alternatives --config java and select Java 1.7

- ElasticSearch:
    - wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.2.1.deb
    - sudo dpkg -i elasticsearch-1.2.1.deb
    - sudo update-rc.d elasticsearch defaults 95 10
    - sudo /etc/init.d/elasticsearch start
    - Any issues see [elasticsearch_webpage](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/setup-service.html)

#### Python Modules:
Note: Workbench is continuously tested with python 2.7. We're currently working on Python 3 support ([Issue 92](https://github.com/SuperCowPowers/workbench/issues/92)).

* cd workbench
* pip install -r requirements.txt
* Go have a large cup of coffee...


## Running It:
#### Server (localhost or server machine)
<pre>
$ cd workbench
$ ./workbench
</pre>
#### Example Clients (use -s for remote server)
There are about a dozen example clients showing how to use workbench on pcaps, PEfiles, pdfs, and log files. We even has a simple nodes.js client (looking for node devs to pop some pull requests :).
<pre>
$ cd workbench/clients
$ python simple_workbench_client.py [-s tcp://mega.server.com]
</pre>

## Testing:
Unit testing and sub-pipeline tests
<pre>
$ cd workbench/server/workers
$ ./runtests
</pre>
      
Full pipeline tests (clients exercise a larger set of components)
<pre>
$ cd workbench/clients
$ ./runtests
</pre>

### Benign Error
We have no idea why occasionaly you see this pop up in the server output. To our knowledge it literally has no impact on any functionality or robustness. If you know anything about this please help us out by opening an issue and pull request. :)
<pre>
ERROR:zerorpc.channel:zerorpc.ChannelMultiplexer, unable to route event:
_zpc_more {'response_to': '67d7df3f-1f3e-45f4-b2e6-352260fa1507', 'zmqid':
['\x00\x82*\x01\xea'], 'message_id': '67d7df42-1f3e-45f4-b2e6-352260fa1507',
'v': 3} [...]
</pre>
### VirusTotal Warning
The vt_query.py worker uses a shared 'low-volume' API key provided by SuperCowPowers LLC. When running the vt_query worker the following warning happens quite often:

    "VirusTotal Query Error, no valid response... past per min quota?"
If you'd like to use the vt_query worker on a regular basis, you'll have to put your own VirusTotal API key in the workbench/server/config.ini file.
<br>

## Contributions/Support/Getting Involved
Workbench is committed to providing open source security software. If you're a developer looking to chip-in or want to support the project please contact us at <support@supercowpowers.com> or visit one of the links below:
<img style="border:1px solid #888888"; src="http://raw.github.com/supercowpowers/workbench/master/images/tshirt_back.jpg" width=150 align="right">
<img style="border:1px solid #888888"; src="http://raw.github.com/supercowpowers/workbench/master/images/tshirt_front.jpg" width=150 align="right">

- Users email list: [workbench-users](https://groups.google.com/forum/#!forum/workbench-users)
- Developer email list: [workbench-devs](https://groups.google.com/forum/#!forum/workbench-devs)
- Feature requests: [issue tracker](https://github.com/SuperCowPowers/workbench/issues)
- **Earn a T-Shirt!**: All issues have cow points, get 100+ for T
- **Buy a T-Shirt!**: [SuperCowPowers](http://www.supercowpowers.com/#about)
- Donate: [SuperCowPowers](http://www.supercowpowers.com/#about)

#### Git Development Model
We're going to use the 'GitHub Flow' model.

- To work on something new, create a descriptively named branch off of master (ie:new-oauth2-scopes)
- Commit to that branch locally and regularly push your work to the same named branch on the server
- When you need feedback or help, or you think the branch is ready for merging, open a pull request
- After someone else has reviewed and signed off on the feature, you can merge it into master

#### Git Example
    $ git checkout -b my-awesome
    $ git push -u origin my-awesome
    $ <code for a bit>; git push
    $ <code for a bit>; git push
    $ Go to github and hit 'New pull request'



## Additional Information
For additional information on the following subjects:
 
* Detailed Project Description
* Configuration File Information
* Optional Tools
* Making your own Worker
* Making your own Client
* Running the IPython Notebooks
* Workbench Conventions
* Test Coverage
* Bounties (Rewards for contributing to Workbench)
* Dependency Installation Errors
* Deprecated Stuff

Please see [README_more.md](README_more.md)