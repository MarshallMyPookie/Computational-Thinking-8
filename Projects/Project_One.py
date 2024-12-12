###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("8 mile rd")

q1 = codesters.Square (100, 100, 200, 'green')
q2 = codesters.Square (-100, 100, 200, 'blue')
q3 = codesters.Square (-100, -100, 200, 'red')
q4 = codesters.Square (100, -100, 200, 'purple')


s1 = codesters.Sprite ("mrbeano", 100, 100)
s1.set_size(0.25)
s2 = codesters.Sprite ("cardinal", -100, -100)
s2.set_size(0.5)
s3 = codesters.Sprite("radal", 100, -100)
s3.set_size(0.5)
s4 = codesters.Sprite("Shady",-80, 75)
s4.set_size(0.25)

message1 = codesters.Text("Ren",0, 220, "red")
message2 = codesters.Text("Bottom Tekst", 0,-220, "red")