# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:18:40 2025

@author: takau
"""

import pygame
import random
import sys
import time

# Initialize Pygame
pygame.init()
pygame.font.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class SushiWord:
    def __init__(self, text, x, y, speed):
        self.text = text
        self.x = x
        self.y = y
        self.speed = speed
        self.current_index = 0
        self.is_completed = False
        self.is_active = False

class SushiTypingGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Sushi Typing Game")
        
        # Fonts
        self.font = pygame.font.SysFont('Arial', 32)
        self.small_font = pygame.font.SysFont('Arial', 24)
        
        # Game state
        self.words = []
        self.score = 0
        self.time_left = 60  # 60 seconds game time
        self.game_active = False
        self.start_time = 0
        
        # Word bank (can be expanded)
        self.word_bank = [
            "sushi", "maki", "temaki", "uramaki", "nigiri",
            "wasabi", "ginger", "sake", "tamago", "ebi",
            "maguro", "salmon", "tuna", "rice", "nori"
        ]
        
        # Game settings
        self.spawn_timer = 0
        self.spawn_delay = 2000  # milliseconds between word spawns
        
    def spawn_word(self):
        word = random.choice(self.word_bank)
        x = WINDOW_WIDTH
        y = random.randint(100, WINDOW_HEIGHT - 100)
        speed = random.uniform(2, 4)
        self.words.append(SushiWord(word, x, y, speed))
    
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if not self.game_active and event.key == pygame.K_RETURN:
                self.start_game()
                return
            
            if not self.game_active:
                return
                
            # Handle typing
            char = event.unicode.lower()
            for word in self.words:
                if word.is_active and not word.is_completed:
                    if char == word.text[word.current_index]:
                        word.current_index += 1
                        if word.current_index == len(word.text):
                            word.is_completed = True
                            self.score += len(word.text) * 10
                    break
                elif not word.is_active and not word.is_completed:
                    if char == word.text[0]:
                        word.is_active = True
                        word.current_index = 1
                        break
    
    def start_game(self):
        self.game_active = True
        self.score = 0
        self.time_left = 60
        self.words.clear()
        self.start_time = time.time()
        
    def update(self):
        current_time = pygame.time.get_ticks()
        
        if self.game_active:
            # Update time
            self.time_left = max(60 - (time.time() - self.start_time), 0)
            
            # Spawn new words
            if current_time - self.spawn_timer > self.spawn_delay:
                self.spawn_word()
                self.spawn_timer = current_time
            
            # Update word positions
            for word in self.words[:]:
                if not word.is_completed:
                    word.x -= word.speed
                    if word.x < -100:  # Word went off screen
                        self.words.remove(word)
                else:
                    self.words.remove(word)
            
            # Check game over
            if self.time_left <= 0:
                self.game_active = False
    
    def draw(self):
        self.screen.fill(WHITE)
        
        if not self.game_active:
            if self.time_left <= 0:  # Game over screen
                game_over_text = self.font.render(f"Game Over! Score: {self.score}", True, BLACK)
                restart_text = self.small_font.render("Press ENTER to play again", True, BLACK)
                self.screen.blit(game_over_text, 
                    (WINDOW_WIDTH//2 - game_over_text.get_width()//2, 
                     WINDOW_HEIGHT//2 - game_over_text.get_height()//2))
                self.screen.blit(restart_text, 
                    (WINDOW_WIDTH//2 - restart_text.get_width()//2, 
                     WINDOW_HEIGHT//2 + 50))
            else:  # Start screen
                start_text = self.font.render("Press ENTER to start", True, BLACK)
                self.screen.blit(start_text, 
                    (WINDOW_WIDTH//2 - start_text.get_width()//2, 
                     WINDOW_HEIGHT//2 - start_text.get_height()//2))
        else:
            # Draw HUD
            score_text = self.small_font.render(f"Score: {self.score}", True, BLACK)
            time_text = self.small_font.render(f"Time: {int(self.time_left)}s", True, BLACK)
            self.screen.blit(score_text, (10, 10))
            self.screen.blit(time_text, (WINDOW_WIDTH - 150, 10))
            
            # Draw words
            for word in self.words:
                # Draw completed portion in green
                if word.current_index > 0:
                    completed_text = self.font.render(
                        word.text[:word.current_index], True, GREEN)
                    self.screen.blit(completed_text, (word.x, word.y))
                
                # Draw remaining portion in black or blue if active
                remaining_text = self.font.render(
                    word.text[word.current_index:], True, 
                    BLUE if word.is_active else BLACK)
                self.screen.blit(remaining_text, 
                    (word.x + self.font.size(word.text[:word.current_index])[0], word.y))
        
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_input(event)
            
            self.update()
            self.draw()
            clock.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SushiTypingGame()
    game.run()