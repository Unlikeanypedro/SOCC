class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        array = nums1 + nums2
        array.sort()

        if ((m + n) % 2) != 0:
            media = array[(len(array) // 2) if len(array) // 2 > 0 else 0 ] 

        else:
            med1 = array[(len(array) // 2 )]
            med2 = array[(len(array) // 2 )-1]
            media = (med1 + med2) / 2.0
            
        return media
