#!/usr/bin/env python

# Hello World in GIMP Python

from gimpfu import *

def flat_icon_generator(name, size, color, filename) :
	
	width = int(size)
	height = int(size)
	
	# Create a new image
	img = gimp.Image(width, height, RGB)
	
	# Save the current foreground color:
	pdb.gimp_context_push()
	
	# Set the icon color
	gimp.set_foreground(color)
	
	# Create a new layer
	backgroud = gimp.Layer(img, "Icon color", width, height, RGB_IMAGE, 100, NORMAL_MODE)
	img.add_layer(backgroud, 0)
	
	# Fill the layer with transparency color
	pdb.gimp_layer_add_alpha(backgroud)
	pdb.gimp_drawable_fill(backgroud, 3)
	
	# Fill the layer with the input color
	pdb.gimp_image_select_round_rectangle(img, 0, 0, 0, width, height, 50, 50)
	pdb.gimp_edit_bucket_fill(backgroud, 0, 0, 100, 0, False, 0, 0)
	pdb.gimp_selection_clear(img)
	
	# Set up an undo group, so the operation will be undone in one step.
	pdb.gimp_undo_push_group_start(img)
	
	# Add the icon image, colorize to white, resize and add to image
	icon_layer = pdb.gimp_file_load_layer(img, filename)
	img.add_layer(icon_layer, 0)
	pdb.gimp_colorize(icon_layer, 180, 50, 100)
	pdb.gimp_layer_scale(icon_layer, 110, 110, False)
	
	# Close the undo group.
	pdb.gimp_undo_push_group_end(img)
	
	# Create a new image window
	gimp.Display(img)
	
	# Create a new image window
	pdb.gimp_displays_flush()
	
	# Restore the old foreground color
	pdb.gimp_context_pop()

register(
	"flat_icon_generator",
	"Flat Icon Generator",
	"Create a new flt icon with your image",
	"Giuseppe Caliendo",
	"Giuseppe Caliendo",
	"2014",
	"Flat Icon...",
	"", # Create a new image, don't work on an existing one
	[
		(PF_STRING, "name", "File name", "Foo"),
		(PF_SPINNER, "size", "Icon size", 144, (1, 3000, 1)),
		(PF_COLOR, "color", "Background color", (1.0, 0.0, 0.0)),
		(PF_FILE, "filename", "Icon file", "")
	],
	[],
	flat_icon_generator, menu="<Image>/File/Create")

main()
