# Idea is to start from the end, then store the next hop on shortest path, given incoming direction and number of steps in that direction.
# Then go back through the blocks. When looking for best path from n,m find a first one by taking shortest path. (This will be the lower bound). 
# So for each block there are 12 different optimal paths. Just store them all and find them all.
# For each direction and when the hop to the block is the first, second of thrid hop in that direction.