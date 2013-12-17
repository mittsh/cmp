cmp
===

A simple Python function to list differences between 2 objects recursively (list, dict, or values).

Usage
=====

Simply call: `cmp` passing 2 objects as arguments, e.g.

	cmp(a, b)

It will return a `list` of `ComparisonDifference` objects. Each of those objects have a `reason` property and a `path` that indicates the path to follow to get the error.
