# Browser History Using a Doubly Linked List
#
# This program simulates how a web browser tracks page history.
# It allows three main operations:
#
# visit(url)    -> Visit a new page
# back(steps)   -> Move backward through history
# forward(steps)-> Move forward through history
#
# The history is implemented using a **doubly linked list**.
#
# Each node represents a webpage and stores:
#
# data : the URL of the page
# prev : the page visited before it
# next : the page visited after it
#
# Example structure:
#
# home <-> yt.com <-> test.com <-> tech.com
#
# If the current page is "tech.com":
#
# home <-> yt.com <-> test.com <-> tech.com
#                                   ^
#                                 current
#
#
# Why a Doubly Linked List?
#
# Browsers need to move both directions through history.
#
# back()    -> move to previous page
# forward() -> move to next page
#
# With a doubly linked list:
#
# current = current.prev   (go back)
# current = current.next   (go forward)
#
# Both operations are O(1).
#
#
# Visiting a New Page
#
# When a user visits a new page, something important happens:
#
# The **forward history must be cleared**.
#
# Example:
#
# home -> yt.com -> test.com -> tech.com
#                          ^
#                        current
#
# If the user presses back once:
#
# home -> yt.com -> test.com -> tech.com
#                ^
#              current
#
# If the user now visits "x.com":
#
# home -> yt.com -> test.com -> x.com
#
# The old forward history ("tech.com") disappears.
#
# This behavior matches real browsers.
#
#
# In this implementation, forward history is cleared automatically
# because we overwrite the current node's "next" pointer:
#
# current.next = Node(url, current)
#
# This disconnects any nodes that were previously ahead.
#
#
# Back Operation
#
# back(steps) moves left through the list using "prev".
#
# Example:
#
# home <-> yt.com <-> test.com <-> tech.com
#                                   ^
#                                 current
#
# back(2)
#
# home <-> yt.com <-> test.com <-> tech.com
#          ^
#        current
#
# The loop stops if:
# - we reach the homepage (prev is None)
# - or we run out of steps
#
#
# Forward Operation
#
# forward(steps) moves right through the list using "next".
#
# Example:
#
# home <-> yt.com <-> test.com <-> tech.com
#          ^
#        current
#
# forward(1)
#
# home <-> yt.com <-> test.com <-> tech.com
#                     ^
#                   current
#
# The loop stops if:
# - there is no next page
# - or we run out of steps
#
#
# Time Complexity
#
# visit(url)      O(1)
# back(steps)     O(steps)
# forward(steps)  O(steps)
#
# Space Complexity: O(n) - visiting a page creates a node
#
#
# Key Idea
#
# The "current" pointer always represents the page the user is
# currently viewing.
#
# Navigation simply moves this pointer through the doubly linked list.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class BrowserHistory(object):

    def __init__(self, homepage):
        self.current = Node(homepage)


    def visit(self, url):
        self.current.next = Node(url, self.current)
        self.current = self.current.next


    def back(self, steps):
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1

        return self.current.data
    

    def forward(self, steps):
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1

        return self.current.data



if __name__ == "__main__":
    b = BrowserHistory("home")
    b.visit("yt.com")
    b.visit("test.com")
    b.visit("tech.com")

    print("current:", b.current.data)
    back_2 = b.back(2)
    print("After going back 2, current is now:", back_2)
    forward_1 = b.forward(1)
    print("After going forward 1, current is now:", forward_1)





# Optimal Array-Based Solution
#
# Although the doubly linked list works well conceptually, an even
# better approach for this problem uses a dynamic array (Python list).
#
# Instead of storing nodes with "prev" and "next" pointers, we store
# visited pages in a list and track positions using indexes.
#
# Example history stored in an array:
#
# ["home", "yt.com", "test.com", "tech.com"]
#
# We track two important indexes:
#
# cur  : the current page
# last : the last valid page in the history
#
#
# Example state:
#
# history = ["home", "yt.com", "test.com", "tech.com"]
# cur = 3
# last = 3
#
# "tech.com" is the current page.
#
#
# Going Back
#
# Instead of walking through nodes, we simply move the index:
#
# cur = max(0, cur - steps)
#
# Example:
#
# history = ["home", "yt.com", "test.com", "tech.com"]
# cur = 3
#
# back(2)
#
# cur = 1
#
# Current page = "yt.com"
#
#
# Going Forward
#
# Forward navigation also just moves the index:
#
# cur = min(last, cur + steps)
#
# Example:
#
# cur = 1
# forward(1)
#
# cur = 2
#
# Current page = "test.com"
#
#
# Visiting a New Page
#
# Visiting a page after going back must erase forward history.
#
# Instead of deleting elements from the array, the optimal solution
# simply overwrites the next slot and updates "last".
#
# Example:
#
# history = ["home", "yt.com", "test.com", "tech.com"]
# cur = 1
# last = 3
#
# Current page = "yt.com"
#
# visit("x.com")
#
# cur += 1
# history[cur] = "x.com"
# last = cur
#
# Now the logical history becomes:
#
# ["home", "yt.com", "x.com"]
#
# The old forward pages still exist in memory but are ignored
# because "last" marks the true end of valid history.
#
#
# Why This Is More Optimal
#
# A naive array implementation might remove forward history using
# slicing:
#
# history = history[:cur]
#
# However, slicing copies elements and takes O(n) time.
#
# The optimal approach avoids copying the array by reusing existing
# positions and tracking the valid range with "last".
#
#
# Complexity Comparison
#
# Doubly Linked List:
#
# visit(url)      O(1)
# back(steps)     O(steps)
# forward(steps)  O(steps)
#
#
# Optimal Array Solution:
#
# visit(url)      O(1) amortized
# back(steps)     O(1)
# forward(steps)  O(1)
#
#
# Key Insight
#
# The array solution does not physically remove forward history.
# Instead, it logically ignores it by tracking where valid history
# ends.

class BrowserHistoryOptimal:
    
    def __init__(self, homepage):
        self.history = [homepage]
        self.cur = 0
        self.last = 0


    def visit(self, url):
        self.cur += 1

        # If we're extending the array
        if self.cur == len(self.history):
            self.history.append(url)
        else:
            # Reuse the existing slot instead of slicing
            self.history[self.cur] = url

        # Mark the end of valid history
        self.last = self.cur


    def back(self, steps):
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]


    def forward(self, steps):
        self.cur = min(self.last, self.cur + steps)
        return self.history[self.cur]