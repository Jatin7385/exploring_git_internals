# Where Are My Git Branches Actually Stored? Understanding Git Internals
## Introduction
Git is one of the most ubiquitous tools in modern software development, yet many developers use it every day without understanding what happens behind the scenes. As a curious engineer, I wanted to explore Git's internals by examining what actually happens in the .git directory when we run commands like git add . and git commit -m ''.
The creator of Git is Linus Torvalds, who also created Linux. After watching a video showing Linus's impressive workspace with a treadmill desk, I thought about how this one person created two of the most widely used pieces of software in the world. Thought, why not try to understand how Git actually works under the hood.

This repo contains 2 .py files.
  - extract_blob.py : Is used to extract an actual blob that git creates to store the content of a version of test.txt.
  - create_blob.py : Is used to create a replica blob in the way that git creates and stores one to keep a track of a version of test.txt

To verify both, we use "git cat-file -p <sha-1_hash>" which prints the actual contents of the file. A lot of the exploration is done directly on the cli, playing around with the git commands, and seeing what happens in the .git folder. I will hopefully soon upload a blog 
on Medium and tag it here.
