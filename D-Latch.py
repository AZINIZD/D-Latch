class DLatch:
    def __init__(self):
        self.D = 0
        self.Clk = 0
        self.Q = 0

    def update(self):
        if self.Clk:
            self.Q = self.D

# Example usage
latch = DLatch()

# Set D = 1, Clk = 1
latch.D = 1
latch.Clk = 1
latch.update()
print("After setting D=1, Clk=1:", latch.Q)  # Output should be 1

# Set Clk = 0 (should not change Q)
latch.D = 0
latch.Clk = 0
latch.update()
print("After setting D=0, Clk=0:", latch.Q)  # Output should still be 1

# Set Clk = 1 (should update Q to D)
latch.D = 0
latch.Clk = 1
latch.update()

print("After setting D=0, Clk=1:", latch.Q)  # Output should be 0
