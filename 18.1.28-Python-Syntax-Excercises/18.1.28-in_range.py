def in_range(nums, lowest, highest):
    for num in nums:
        if lowest <= num <= highest:
            print(num,"Fits")
in_range([10, 20, 30, 40], 15, 30)

