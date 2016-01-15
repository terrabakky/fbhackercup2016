#!/usr/bin/env python
# Author: Tyler K Johnson 2016
# Facebook Hacker Cup Question 1, 2016

from collections import defaultdict
from math import hypot


input_coords = []

def process_input():
	f = open('official_input.txt','rU')

	# get rid of first line of file that holds number of questions
	f.readline()

	# split on new line
	f = f.read().split('\n')

	for i in f:
		if len(i.split()) == 1:
			input_coords.append(set())
		if len(i.split()) == 2:
			input_coords[-1].add(tuple(float(point) for point in i.split()))

process_input()


def calculate_distance(origin_point):
	for point in coords:
		# skip points checking themselves
		if point == origin_point:
			continue

		# calculate the distance between the two points
		distance = hypot(origin_point[0] - point[0], origin_point[1] - point[1])

		distances[origin_point][distance].add(point)

		distances[point][distance].add(origin_point)


def check_boomerang():
	# get each point
	boomerangs = set()
	score = 0

	for point, values in distances.iteritems():
		for distance in values:
			for coord in distances[point][distance]:
				for result in distances[coord][distance]:
					if result != point and result != coord:
						if tuple(sorted([point, coord, coord, result])) in boomerangs:
							continue
						else:
							boomerangs.add(tuple(sorted([point, coord, coord, result])))
							score += 1
	return score



for problem_number, coords in enumerate(input_coords):
	distances = defaultdict(lambda : defaultdict(set))

	map(calculate_distance, coords)

	total = check_boomerang()
	print "Case #%s: %s" % (problem_number+1, total)

