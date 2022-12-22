"""Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print
    - is number between designated lowest/highest (15, 30)?
    - lowest/highest is not meant to reflect nums inside
      the list within the range method!

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits

      - because 20/30 fits are within the range of 15/30
        designated as above.
    """
def in_range(nums, lowest, highest):
    for num in nums:
        if num >= lowest and num <= highest:
            print(num, "fits")

in_range([10, 20, 30, 40, 50], 15, 30)    
        
