import random
import string

class StreakHead:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.length = random.randint(3, 7)
        self.width = width
        self.height = height
        self.streak = random.choices(string.ascii_letters, k=self.length)
    
    def update(self):
        if self.y + 1 < self.height:
            self.y += 1
            head = self.streak[0]
            self.streak = random.choices(string.ascii_letters, k=self.length)
            self.streak[0] = head
            return True
        else:
            return False
        
    def get_streak(self):
        return self.streak
    
    def get_length(self):
        return self.length
    
    def __str__(self):
        return f'Head at ({self.x}, {self.y})'
    
    def __repr__(self):
        return self.__str__()

def pmatrixCLI(width, height, frames_count):
    frame = [[' ' for _ in range(width)] for _ in range(height)]
    all_frames = []
    streaks = []
    
    for x in range(width):
        if random.randint(0, 10) > 4:
            streaks.append(StreakHead(0, x, width, height))
        else:
            streaks.append(None)
    
    for _ in range(frames_count):
        for streak in streaks:
            if streak:
                # Clear previous position
                for i in range(streak.length):
                    if streak.y - i >= 0 and streak.y - i < height:
                        frame[streak.y - i][streak.x] = ' '
                
                # Update streak position
                if streak.update():
                    # Draw new position
                    for i in range(streak.length):
                        if streak.y - i >= 0 and streak.y - i < height:
                            frame[streak.y - i][streak.x] = streak.streak[i]
                else:
                    # Restart streak
                    streak.x = random.randint(0, width - 1)
                    streak.y = 0
                    streak.streak = random.choices(string.ascii_letters, k=streak.length)
        
        
        all_frames.append('```' + '\n'.join([''.join(row) for row in frame]) + '```')
    
    return all_frames
        

if __name__ == "__main__":
    matrix = pmatrixCLI(60, 20, 100)
