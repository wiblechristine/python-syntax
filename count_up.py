#Print all numbers from start up to and including stop.
#For example:

   #calling function count_up(5, 7)

   #should print in the shell:

     #   5
     #   6
     #   7
    
def count_up(start, stop):
    while start <= stop:
        print(start)
        start = start + 1

count_up(5, 7)        
