class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Determine the smaller Arr

        # Get the partition from the smaller array

        # Determine a half val which comes from the total of lengths of both arrs

        # iterate over the smaller array to find the correct partition, do so until
        # the mid value is less than the right partitions left most value
        # and if the others arrays mid value is less than or equal to the leftmost value
        # in the other arrays right partition 
        # so that could be nums[m+1]

        A,B = nums1,nums2

        if len(B) < len(A):
            A,B = B,A
        
        l,r = 0,len(A)- 1
        total = len(A) + len(B)
        half = total // 2
        median = 0
        while True: 
            Amid = (l+r) // 2 # 3 
            ApartLength = Amid # 3
            Bpartlength = half - Amid - 2 # 3 
            Aleft = A[Amid] if Amid >= 0 else float('-infinity')
            Aright = A[Amid+1] if Amid+1 <len(A) else float('infinity')
            Bleft = B[Bpartlength] if Bpartlength >= 0 else float('-infinity')
            Bright = B[Bpartlength + 1] if Bpartlength + 1 <len(B) else float('infinity')
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright,Bright)
                # even
                return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            elif Aleft > Bright:
                r = Amid - 1
            else:
                l = Amid + 1