## SOLUTION

Upper 3 bits of hash are left untouched, you can use them to find next 3 bits of original data and so on. If you don't feel like bitfidling hero, you can do it in-place, bit-by-bit with ofset of 3 bits. See [solution.rb](solution.rb).