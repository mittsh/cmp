class ComparisonDifference(object):
	def __init__(self, reason, path):
		self.reason = reason
		self.path = path
	def __unicode__(self):
		return u'{reason} (path: {path})'.format(reason=self.reason, path='.'.join([str(x) for x in self.path]))

def cmp(a,b, verbose = False, path = []):
	differences = []
	
	# Check if both objects are same type
	if type(a) != type(b):
			differences.append(ComparisonDifference(u'Type Mismatch: {a} != {b}'.format(a=type(a), b=type(b)), path))
	
	# Compare lists
	elif type(a) == list:
		if verbose:
			print(u'[l] Compare Lists: {a} vs. {b}'.format(a=len(a), b=len(b)))
		
		# Check lenghts
		if len(a) != len(b):
			differences.append(ComparisonDifference(u'Mismatch in list length', path))
		
		# Compare internally
		else:
			for i in range(len(a)):
				differences += cmp(a[i], b[i], verbose, path + [i])
	
	# Compare dicts
	elif type(a) == dict:
		if verbose:
			print(u'[d] Compare Dicts: {a} vs. {b}'.format(a=','.join(a.keys()), b=','.join(b.keys())))
		
		# Check lengths
		if len(a) != len(b):
			differences.append(ComparisonDifference(u'Mismatch in dict length', path))
		
		# Compare internally
		else:
			for key in a:
				differences += cmp(a[key], b[key], verbose, path + [key])
	
	# Compare values
	else:
		if verbose:
			print(u'[v] Compare Values: "{a}" (length: {la}, type: {ta}) vs. "{b}" (length: {lb}, type: {tb})'.format(a=a, b=b, ta=type(a).__name__, tb=type(b).__name__, la=len(a) if type(a) in (str, unicode) else 0, lb=len(b) if type(b) in (str, unicode) else 0))
		
		if a != b:
			differences.append(ComparisonDifference(u'Values "{a}" and "{b}" mismatch'.format(a=a, b=b), path))
	
	# Return differences
	return differences
