#!/usr/bin/python

#This is a funcky cli tool for fucking with subdomain lists

import argparse
import string
import sys

alist = []
freqlist = []

def readFile(fname):
	try:
		with open(fname) as f:
			data = f.read().splitlines()
	except IOError:
		print 'Error reading file! file-> '+fname
	return data

def sortDictByFrequency(fd):
	z = [(fd[k], k) for k in fd]
	z.sort()
	z.reverse()
	return z

def subLength(sub):
	return len(string.split(sub, '.'))

def getDomain(subs):
	s = subs[0]
	ss = string.split(s, '.')[-2:]
	return '.'.join(ss)

def getSubSubs(sub, z, domain):
	if z > 2:
		ss = string.split(sub, '.')
		ss.pop(0)
		s = '.'.join(ss)
		if s != domain:
			alist.append(s)
		getSubSubs(s, subLength(s), domain)
	else:
		return

def getFrequencyList(subs, domain):
	for s in subs:
		getSubSubs(s, subLength(s), domain)
	for a in alist:
		freqlist.append(alist.count(a))
	newlist = dict(set(zip(alist, freqlist)))
	return sortDictByFrequency(newlist)

if __name__ == '__main__':
	parse = argparse.ArgumentParser()
	parse.add_argument('-s', '--subs', type=str, default='',
						help='A list of subdomains')
	parse.add_argument('-l', '--lists', type=str, default='list.txt',
						help='A list of already scraped subdomains')
	parse.add_argument('-g', '--gen', action='store_true', default=False,
						help='Generate the lists')
	parse.add_argument('-1', '--genone', action='store_true', default=False,
						help='Display only single entries from list')
	parse.add_argument('-w', '--wildcard', action='store_true', default=False,
						help='Generate a list from only wildcard cert domains')
	parse.add_argument('-gs', '--getsubs', action='store_true', default=False,
						help='Get a list of unique subdomains from list')
	parse.add_argument('-gu', '--geturls', action='store_true', default=False,
						help='Generate a list of urls from subdomains')
	args = parse.parse_args()

	if len(sys.argv) <= 1:
		parse.print_help()
		sys.exit(0)

	if args.gen and args.subs == '':
		lists = readFile(args.lists)
		finalist = getFrequencyList(lists, getDomain(lists))
		for i,j in finalist:
			if i >= 2 and j != getDomain(lists) and not args.genone:
				print j + '-->   '+str(i)
			elif i == 1 and j != getDomain(lists) and args.genone:
				print j + '-->   '+str(i)
	
	elif args.gen and args.subs != '':
		lists = readFile(args.lists)
		subs = readFile(args.subs)
		finalist = getFrequencyList(lists, getDomain(lists))
		for i, j in finalist:
			for x in subs:
				print x + '.' + j
	
	if args.subs == '' and args.wildcard:
		lists = readFile(args.lists)
		for i in lists:
			if '*' in i:
				print i

	elif args.subs != '' and args.wildcard:
		lists = readFile(args.lists)
		subs = readFile(args.subs)
		for i in lists:
			if '*' in i:
				for j in subs:
					print i.replace('*', j)
	
	if args.getsubs:
		lists = readFile(args.lists)
		for i in lists:
			new = string.split(i, '.')
			for j in new:
				if j != '*':
					alist.append(j)
				if '-' in j:
					jj = string.split(j, '-')
					for z in jj:
						alist.append(z)
		freqlist = sorted(set(alist))
		for i in freqlist:
			print i

	if args.geturls:
		lists = readFile(args.lists)
		for i in lists:
			if '*' not in i:
				print 'http://'+i+'/'
				print 'https://'+i+'/'
