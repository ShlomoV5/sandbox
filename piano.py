# todo
# learn the pyaudio library and play with it
# using cli only, no pygame.
# later, pygame.

import pygame
import numpy as np
import pyaudio

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Piano App')

# Define piano keys and their corresponding frequencies
keys = [
    ('C', 261.63), ('D', 293.66), ('E', 329.63),
    ('F', 349.23), ('G', 392.00), ('A', 440.00), ('B', 493.88)
]

# Define the size and position of keys
key_width = WIDTH // len(keys)
key_height = HEIGHT

# Initialize PyAudio
p = pyaudio.PyAudio()

def play_tone(frequency, duration=1.0, sample_rate=44100):
    """Play a tone with a given frequency and duration."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = np.sin(frequency * t * 2 * np.pi)
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)
    
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, output=True)
    stream.write(audio.tobytes())
    stream.stop_stream()
    stream.close()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            key_index = x // key_width
            if 0 <= key_index < len(keys):
                frequency = keys[key_index][1]
                play_tone(frequency)
    
    # Draw the piano keys
    window.fill((255, 255, 255))
    for i, (note, freq) in enumerate(keys):
        key_rect = pygame.Rect(i * key_width, 0, key_width, key_height)
        pygame.draw.rect(window, (0, 0, 0), key_rect, 1)
        font = pygame.font.Font(None, 36)
        text = font.render(note, True, (0, 0, 0))
        window.blit(text, (i * key_width + key_width // 3, key_height // 2))
    
    pygame.display.flip()

pygame.quit()
p.terminate()