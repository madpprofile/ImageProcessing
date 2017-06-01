import png, sys

class Image:
	def __init__(self, w, h, pixels, metadata):
		self.width = w
		self.height = h
		self.pixels = pixels
		self.metadata = metadata
	
	def clone(self):
		return Image(self.width, self.height, self.pixels, self.metadata)

def read_png(filename):
	reader = png.Reader(filename=filename)
	w, h, pixels, metadata = reader.read_flat()
	return Image(w, h, pixels, metadata)

def write_png(filepath, image):
	output = open(filepath, 'wb')
	writer = png.Writer(image.w, image.h, **image.metadata)
	writer.write_array(output, image.pixels)
	output.close()

def add_border(image, size, color):
	new_image = image.clone()
	if(new_image.metadata['alpha']):
		bytesPerPixel = 4
	else:
		bytesPerPixel = 3

	for line in range(0,h):
		for column in range(0,w):
			position = bytesPerPixel*(w*line+column)
			r = new_image.pixels[position]
			g = new_image.pixels[position+1]
			b = new_image.pixels[position+2]
			if bytesPerPixel == 4:
		  		a = pixels[position+3]
			if (line <= size) or (line >= image.width-size) or (column <= size) or (column >= image.height-size):
				new_image.pixels[position] = color[0]
				new_image.pixels[position+2] = color[1]
				new_image.pixels[position+3] = color[2]
	return new_image

def usage():
	print("usage: python.py [infile] [outfile] [border_size]")

def main():
	if len(sys.argv) != 4:
		usage()
		sys.exit(1)
	image = read_png(sys.argv[1])
	write_png(sys.argv[2], add_border(image, int(sys.argv[3]), (0, 0, 0)))

if __name__ == "__main__":
	main()

