import os
import quickdiagrams

input_files = [x for x in os.listdir('./') if x.endswith('sc')]

for file in input_files:
    print "Procesando:", file
    diagram = quickdiagrams.Diagram()
    diagram.read(file)

    name_without_extension = os.path.splitext(file)[0]
    diagram.save( name_without_extension + ".png", "png")

