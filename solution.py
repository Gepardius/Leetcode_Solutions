class Solution():
    # Rotate an array to the right by 'k' steps
    def rotate_array(self, nums, k):
        
        for i in range(k):
            element = nums[-1]
            nums.pop()
            nums.insert(0, element)

        return nums
    
    # Trap rainwater using an array of heights
    def trap(self, nums):
        
        water = 0
        
        next_iterator = 0
        for i in range(len(nums)):
            
            if i != 0 and i != len(nums)-1 and i >= next_iterator:
                
                if nums[i] != 0: 
                    element = nums[i]
                    
                    blacks = 0
                    for j in range(len(nums)):
                        if j > i:
                            
                            if nums[j] >= nums[i]:
                                
                                right_element = nums[j]
                                steps = j - i - 1
                                break
                            
                            blacks += nums[j]
                    water = water + min(element, right_element)*steps - blacks
                    next_iterator = j
                    pass
                            

                
        
        return water
    
    # Find the maximum profit by buying and selling stocks
    def stock_profit(self, prices):
        
        
        low = 0
        high = 1
        max_profit = 0
        while high < len(prices):
            current_profit = prices[high] - prices[low]
            if prices[low] < prices[high]:
                max_profit = max(max_profit, current_profit)
            else:
                low = high
            
            high += 1
        return max_profit
            
    # Find the maximum difference between two elements in an array
    def maximum_difference(self, nums):
        
        maximum_dif = -1
        left = 0
        right = 1

        while right < len(nums):
            current_diff = nums[right] - nums[left]
            if nums[left] < nums[right]:
                maximum_dif = max(current_diff, maximum_dif)
            else:
                left = right
                
            right += 1
                
        
        return maximum_dif
    
    # Find the length of the last word in a string
    def length_string(self, s):
        
        s_list = s.split(" ")
        i = len(s_list)-1
        while i >= 0:
            if s_list[i] != "":
                return len(s_list[i])

            i -= 1
        
        if len(s) == 1:
            return 1
        return 0
    
    # Remove a specified element from an array
    def remove_element(self, nums, val):
        
        final_array = []
        
        for i in range(len(nums)):
            # print(nums[i])
            if nums[i] != val:
                final_array.append(nums[i])
        
        print(final_array)
        return len(final_array)

    # Check if a string is a palindrome
    def isPalindrome(self, s):
        
        isPalindrome = False
        
        left = []
        right = []
        for char in s:
            if char.isalnum():
                left.append(char.lower())
        
        i = len(left) - 1
        while i >= 0:
            right.append(left[i])
            
            i -= 1
        
        if left == right or len(left) == 1:
            isPalindrome = True
        
        return isPalindrome

     # Find all unique triplets in an array that sum to zero
    def three_sum(self, nums):
        
        sum_elements = 1000
        return_list = []
        already_used_list = []
        used_indexes = []
        for i in range(len(nums)):
            first_element = nums[i]
            for j in range(len(nums)):
                if j != i:
                    second_element = nums[j]
                    for k in range(len(nums)):
                        if j != k and k != i:
                            third_element = nums[k]
                            
                            sum_elements = first_element + second_element + third_element 
                            used_index = [i, j, k]
                            used_index = sorted(used_index)
                            
                            used_index_1 = sorted([i, j])
                            used_index_2 = sorted([i, k])
                            used_index_3 = sorted([j, k])
                            
                            if sum_elements == 0 and used_index not in already_used_list and used_index_1 not in used_indexes and used_index_2 not in used_indexes and used_index_3 not in used_indexes:
                                return_list.append([first_element, second_element, third_element])
                                used_indexes.append(used_index_1)
                                used_indexes.append(used_index_2)
                                used_indexes.append(used_index_3)
                                already_used_list.append(used_index)

                                break
                
                if sum_elements == 0:
                    break
        
        print(already_used_list)
        return return_list
    
    # Find all pairs of elements in an array that sum to a target value
    def two_sum(self, nums, target):
        
        final_list = []
        
        for i in range(len(nums)):
            first = nums[i]
            for j in range(len(nums)):
                second = nums[j]
                sum = first + second
                if sum == target and i != j:
                    final_list.append([i, j])
                    return final_list
        
            
        return final_list
    
    # Check if a ransom note can be constructed from a magazine
    def canConstruct_hash(self, ransomNote, magazine):
        
        hash_table = {}
        can_construct = False
        for index, char in enumerate(magazine):
            hash_table[char] = index
        
        used_indexes = []
        for char in ransomNote:
            if char in hash_table:
                used_indexes.append(hash_table[char])
                
        if len(used_indexes) == len(ransomNote):
            can_construct = True
        
        return can_construct
    
    def canConstruct_table(self, ransomNote, magazine):
        
        can_construct = False
        
        magazine_list = []
        for char in magazine:
            magazine_list.append(char)
        
        ransom_list = []
        for char in ransomNote:
            ransom_list.append(char) 
        
        used_indexes = []
        used_letters = []
        
        for i in range(len(ransom_list)):
            ransom_letter = ransom_list[i]
            
            for j in range(len(magazine_list)):
                magazine_letter = magazine_list[j]
                if ransom_letter == magazine_letter and j not in used_indexes and len(used_indexes) < len(ransom_list):
                    used_indexes.append(j)
                    used_letters.append(magazine_list[j])
                    break
            
        
        print(used_letters, ransom_list)
        if len(used_indexes) == len(ransom_list) and used_letters == ransom_list:
            can_construct = True

        return can_construct
    
    # Efficiently check if a ransom note can be constructed from a magazine
    def canConstruct(self, ransomNote, magazine):
        
        letter_dict = {}
        
        for char in magazine:
            if char not in letter_dict:
                letter_dict[char] = 1
            else:
                letter_dict[char] += 1
        
        for char in ransomNote:
            if char in letter_dict:
                if letter_dict[char] > 0:
                    letter_dict[char] -= 1
                else:
                    return False
            else:
                return False

        return True
    
    # Check if there are any duplicates within 'k' distance in an array
    def containsNearbyDuplicate(self, nums, k):
        
        hash_table = {}
        for index, element in enumerate(nums):
          if element in hash_table and abs(index - hash_table[element]) <= k:
            return True
          else:
            hash_table[element] = index

        return False
    
    # Find the length of the longest consecutive elements sequence in an array
    def longestConsecutive(self, nums):
        
        hash_table = {}
        
        for i in range(len(nums)):
            hash_table[nums[i]] = i
        
        print(hash_table)
        streak_list = []
        
        for i in range(len(nums)):
            streak = 1
            current_int = nums[i]
            next_int = current_int + 1
            previous_int =  current_int - 1
            if next_int in hash_table and previous_int not in hash_table:
                streak += 1
                continue_streak = True
                while continue_streak:
                    next_int += 1
                    if next_int in hash_table:
                        streak += 1
                    else:
                        continue_streak = False
                        
                streak_list.append(streak)

        if len(nums) == 1:
            streak = 1
        elif nums != []:
            streak = max(streak_list)
        elif streak_list == []:
            streak = 0
        
            
        return streak
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # used_indexes = []
        # final_list = []
        
        # for i in range(len(strs)):
            
        #     current_string = strs[i]
            
        #     same_strings = []
            
        #     letters = []
        #     for char in current_string:
        #         letters.append(char)
            
        #     if letters == []:
        #         letters = [""]
        #     letters = sorted(letters)
            
        #     if i not in used_indexes:
        #         for j in range(len(strs)):
                    
        #             check_string = strs[j]
        #             check_letters = []
                        
        #             if i != j and j not in used_indexes:
                        
        #                 for character in check_string:
        #                     check_letters.append(character)
                        
        #                 if check_letters == []:
        #                     check_letters = [""]
                        
        #                 check_letters = sorted(check_letters)
                    
        #             if letters == check_letters:
        #                 same_strings.append(check_string)
        #                 used_indexes.append(j)
            
            
        #     same_strings.append(current_string)
            
        #     if i not in used_indexes:
        #         final_list.append(same_strings)
            
        #     used_indexes.append(i)
            
        
        # return final_list
        
        # anagram_map = defaultdict(list)
            
        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        #     anagram_map[sorted_word].append(word)
        
        # return list(anagram_map.values())
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        is_happy = False
        sum_int = str(n)
        
        loop_end = 1000
        while sum_int != "1":
            string_list = []
            for char in sum_int:
                string_list.append(int(char))
            
            print(sum_int)
            current_sum = 0
            for i in range(len(string_list)):
                current_sum = int(current_sum) + int(string_list[i])*int(string_list[i])

            sum_int = str(current_sum)
            loop_end -= 1
            if loop_end < 0:
                break
        
        if sum_int == "1":
            is_happy = True
            
        return is_happy
    
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hash_table = {}
        for i in range(len(numbers)):
            j = i + 1
            hash_table[numbers[i]] = j
        
        for k in range(len(numbers)):
            difference = target - numbers[k]
            if difference in hash_table:
                return sorted([hash_table[difference], k+1])
        
        return []

    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        nums = sorted(nums)
        
        length = len(nums) - 1
        sum_target = 0
        
        count = 0
        while length >= 0:
            current_int = nums[length]
            sum_target = sum_target + current_int
            count += 1
            if sum_target >= target:
                return count
            
            length -= 1
        
        return 0
    
if __name__ == "__main__":
    
    #### move array to the right
    solution_instance = Solution()
    
    # nums = [1,2,3,4,5,6,7]
    # k = 3
    # nums = [-1,-100,3,99]
    # k = 2
    # solution = solution_instance.rotate_array(nums, k)
    # print(solution)
    
    # nums = [0,1,0,2,1,0,1,3,2,1,2,1]
    
    # nums = [0, 1, 0, 0, 0, 5, 0]
    
    # nums = [4,2,0,3,2,5]
    
    # solution = solution_instance.trap(nums)
    # print(solution)
    
    # nums = [7,1,5,3,6,4]
    
    # nums = [2,4,1]
    
    # solution = solution_instance.stock_profit(nums)
    # print(solution)
    
    # nums = [9,4,3,2]
    # solution = solution_instance.maximum_difference(nums)
    # print(solution)
    
    # nums = [2,3,1,1,4]
    # nums = [3,2,1,0,4]
    # nums = [0]
    # solution = solution_instance.jump_game(nums)
    # print(solution)
    
    # s = "   fly me   to   the moon  "
    # s = "a "
    # solution = solution_instance.length_string(s)
    # print(solution)
    
    # nums = [3,2,2,3]
    # solution = solution_instance.remove_element(nums, 2)
    # print(solution)
    
    # s = "0P"
    # solution = solution_instance.isPalindrome(s)
    # print(solution)
    
    # height = [1,1]
    # height = [1,8,6,2,5,4,8,3,7]
    # solution = solution_instance.water_container(height)
    # print(solution)
    
    # nums = [-1,0,1,2,-1,-4]
    # nums = [-2,0,0,2,2]
    # solution = solution_instance.three_sum(nums)
    # print(solution)
    
    # nums = [2,7,11,15]
    # target = 26
    # solution = solution_instance.two_sum(nums, target)
    # print(solution)
    
    # solution = solution_instance.canConstruct("a", "b")
    # print(solution)
    
    # nums = [2,7,11,15]
    # target = 26
    # solution = solution_instance.two_sum(nums, target)
    # print(solution)
    
    # nums =  [1,2,3,1,2,3]
    # k = 2
    # solution = solution_instance.containsNearbyDuplicate(nums, k)
    # print(solution)
    
    # nums = [1, 0, 2, 1, 3, 100, 101, 103]
    # solution = solution_instance.longestConsecutive(nums)
    # print(solution)
    
    # strs = ["",""]
    # solution = solution_instance.groupAnagrams(strs)
    # print(solution)
    
    
    # n = 19
    # solution = solution_instance.isHappy(n)
    # print(solution)
    
    # numbers = [1, 3]
    # target = 4
    # solution = solution_instance.twoSum(numbers, target)
    # print(solution)
    
    numbers = [12,28,83,4,25,26,25,2,25,25,25,12]
    target = 213
    solution = solution_instance.minSubArrayLen(target, numbers)
    print(solution)
