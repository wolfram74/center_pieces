import svgwrite
# mm = svgwrite.mm
mm = 3.54

def to_milimeter(raw):
	output = []
	# mm=3.54
	for item in raw:
		output.append(
			[item[0]*mm, item[1]*mm]
			)
	return output

def make_svg(length):
	pad = 50
	buffer = 50
	height = 100
	shift = (length+pad)/2

	dwg = svgwrite.Drawing(
		'test3.svg', profile='full', 
		size=(
			# '%dmm'%(200+2*pad), 
			# '%dmm'%(100+2*pad) 
			mm*(200+2*pad), 
			mm*(100+2*pad) 
			))

	# dwg.add(dwg.line(
	# 	(5,5), (5,15),
	# 	stroke=svgwrite.rgb(0,0,0, "%")
	# 	))
	# dwg.add(dwg.line(
	# 	(5,15), (25,15),
	# 	stroke=svgwrite.rgb(0,0,0, "%")
	# 	))
	# dwg.add(dwg.line(
	# 	(25,15), (25,5),
	# 	stroke=svgwrite.rgb(0,0,0, "%")
	# 	))

	points = [
		(pad,pad),
		(pad,pad+height),
		(pad+length,pad+height),
		(pad+length,pad),
		(pad+length-10,pad),
		(pad+length-10,pad+height-10),
		(pad+10,pad+height-10),
		(pad+10,pad),
		(pad,pad),
	]
	# points = [
	# 	(pad*mm,pad*mm),
	# 	(pad*mm,(pad+height)*mm),
	# 	((pad+length)*mm,(pad+height)*mm),
	# 	((pad+length)*mm,pad*mm),
	# 	((pad+length-10)*mm,pad*mm),
	# 	((pad+length-10)*mm,(pad+height-10)*mm),
	# 	((pad+10)*mm,(pad+height-10)*mm),
	# 	((pad+10)*mm,pad*mm),
	# 	(pad*mm,pad*mm),
	# ]

	tweaked = to_milimeter(points)
	# tweaked = points

	print(points[0])
	for item in tweaked:
		print(item)

	for ind, point in enumerate(tweaked[:-1]):
		dwg.add(dwg.polyline(
			(point, tweaked[ind+1]),
			stroke=svgwrite.rgb(0,0,0),
			stroke_width=1*mm
			))

	dwg.save()

# L = 150

# center = L/2
# width = 50
# space = 3
# for i in range(10):
# 	x = center-width + i*10
# 	y = x**2/40
# 	next_point = (i, i**2/36)
# 	dwg.add(dwg.line(point, next_point, stroke=svgwrite.rgb(10, 10, 16, '%')))
# 	point=next_point

def main():
	length = 200
	make_svg(length)

if __name__ == '__main__':
	main()