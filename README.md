# NCSA's SANS Holiday Hack Challenge 2017

Here is our team's repository for all tools and reports from this years [SANS Holiday Hack Challenge](https://www.holidayhackchallenge.com/2017/). If you're looking for the 2016 report that's available [here](https://ncsa.github.io/sans-holiday-hack-2016/).

The full readable online report is available at (https://ncsa.github.io/sans-holiday-hack-2017/).

We tried to make this repo as user friendly as possible. Each directory has its own Makefiles. If you run `make` from the root directory it will execute everything for you.

## Tools

This directory contains all the command line tools we created for this challenge. The Makefile will install additional tools that we pulled in from other projects that we found useful.

## Output

This folder is for outputs from the tools and are reused to answer subsequent challenges. The Makefile in here executes a number of the tools from the tools folder and dumps the output here.

## Support Files

This folder has a few files collected from the challenge that we use in some of the scripts.

## Report

This directory contains the final written report. The reports are written in [org-mode](https://orgmode.org/) and the Makefile will generate an html report from those files.
