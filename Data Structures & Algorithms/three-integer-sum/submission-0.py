class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        arr = sorted(nums)
        answer = []

        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            left = i + 1
            right = len(arr) - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    answer.append([arr[i], arr[left], arr[right]])

                    left += 1
                    right -= 1

                    while left < right and arr[left] == arr[left - 1]:
                        left += 1

                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1

        return answer
