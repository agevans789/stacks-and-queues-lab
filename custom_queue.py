import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Add an item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        # FIX: Return only the very first item at index 0, not the entire list
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # Return True if the queue is empty
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        if self.is_empty():
            return None
            
        # 1. Randomly pick a winning customer currently in the queue
        winner = random.choice(self.items)
        
        # 2. Dequeue all items from the front up to and including the winner
        while not self.is_empty():
            current_item = self.dequeue()
            if current_item == winner:
                break
                
        # 3. Return the name of the winning customer
        return winner

