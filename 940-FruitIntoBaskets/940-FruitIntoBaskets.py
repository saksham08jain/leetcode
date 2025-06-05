# Last updated: 5/6/2025, 11:06:44 pm
class Solution:
    def totalFruit(self, tree):
        left = 0  # Start of the window
        last_fruit, second_last_fruit = -1, -1
        last_fruit_count = 0
        max_fruits = 0
        curr_max = 0
        right = 0  # Pointer for the right end of the window

        while right < len(tree):
            fruit = tree[right]
            
            if fruit == last_fruit or fruit == second_last_fruit:
                curr_max += 1
            else:
                curr_max = last_fruit_count + 1  # Start a new window with two types of fruits
            
            if fruit == last_fruit:
                last_fruit_count += 1
            else:
                last_fruit_count = 1
                second_last_fruit = last_fruit
                last_fruit = fruit
            
            max_fruits = max(max_fruits, curr_max)
            right += 1

        return max_fruits

