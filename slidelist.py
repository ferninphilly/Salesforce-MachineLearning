# to run this
# python slidelist.py < html file
# output is a list of slides to print, i.e., command-line arg to decktape
# e.g., 1-2,5,18-20,25-27,29-46,56-60,67-69,71-72,74-96,99-100,106,110,114,117-118,120-121,124-129,132-141,146,152,156,160,163,166,168-169,172,175-176,178-183,191-194,205-210,219,224,229,233,237-240,245-246,249,252,255-261,264,267,269,273,275,280,283,288-292,295,304,307-314,317,320,325,330-332,339,343-344,350,353,356,358-359,362

from __future__ import print_function
import sys

def add_num_or_range(start, end):
    if start == end:
        slide_list.append(str(start))
    else:
        slide_list.append('{}-{}'.format(start, end))

start_slide_num = 1
end_slide_num = 1
incremental = False
slide_list = []

# When we see a new slide (---), we need to wait and see if it
# has incremental bullet points (--). If NOT, i.e., we get to
# the next ---, then we should 

# title
# --- (2) maybe 1-2
# ...
# --- (3) maybe 1-3
# ...
# -- (4) yes 1-3, maybe 4-5
# ...
# -- (5) maybe 5-6
# ...
# --- (6) maybe 5-6
# ...
# --- (7) maybe 5-7
# ...
# -- (8) yes 5-7

for line in sys.stdin:
    if line.startswith('---'): 
        if incremental:
            incremental = False
            # print('*', end_slide_num)
            start_slide_num = end_slide_num
        end_slide_num += 1
        # print('---', start_slide_num, end_slide_num)
    elif line.startswith('--'): 
        if not incremental:
            add_num_or_range(start_slide_num, end_slide_num - 1)
            start_slide_num = end_slide_num - 1
        incremental = True
        start_slide_num += 1
        end_slide_num += 1
        # print('--', start_slide_num, end_slide_num)

add_num_or_range(start_slide_num, end_slide_num)
print(','.join(slide_list))
