# vl-script
Script used to generate objects in .obj format for blender animations.

To use: clone repo and at the bottom of shapeCreate.py enter a supported polygon (triangle, square, pentagon, hexagon, octagon) as well as other inputs
such as number of layers, width, and angle offset (used for rotation per polygon).

Recall that .obj format requires points (denoted as vertex 'v') to be of format: "v x y z" where x, y, z are real numbers.
Recall that .obj format requires edges (denoted as facet 'f') to be of format: "f a b c" where a, b, c, are numbers mapped to vertex listing.

![hexTwise](https://github.com/matthew-curry-var/vl-script/assets/106562383/98747d9d-607b-41d3-9db5-20226f07241b)
