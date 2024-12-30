import cowsay
import sys

my_fish = r'''
\
 \
        /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸)
     `\\´´\¸.·´
'''



if len(sys.argv) == 2:
    # cowsay.turtle(f"Hi, {sys.argv[1]}")
    cowsay.draw(f"Hi, {sys.argv[1]}", my_fish)
else:
    print(f"1 additional argument excpected, {len(sys.argv)-1} provided")
