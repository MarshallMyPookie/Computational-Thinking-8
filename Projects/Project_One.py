###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("underwater")

q1 = codesters.Square (100, 100, 200, 'green')
q2 = codesters.Square (-100, 100, 200, 'blue')
q3 = codesters.Square (-100, -100, 200, "red")
q4 = codesters.Square (100, -100, 200 'yellow')


s1 = codesters.sprite ('mrbeano' 100, 100)
