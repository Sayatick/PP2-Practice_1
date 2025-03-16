import pygame
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎵 Pygame Music Player")

MUSIC_FOLDER = "lab_07/music"

if not os.path.exists(MUSIC_FOLDER):
    print(f"⚠️ Error: The folder '{MUSIC_FOLDER}' does not exist!")
    pygame.quit()
    exit()

songs = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith((".mp3", ".wav"))]
if not songs:
    print("⚠️ No music files found in the 'music/' folder!")
    pygame.quit()
    exit()

current_song_index = 0
is_playing = False
is_paused = False

play_img = pygame.image.load("lab_07/play.png")
stop_img = pygame.image.load("lab_07/stop.png")
next_img = pygame.image.load("lab_07/next.png")
prev_img = pygame.image.load("lab_07/prev.png")

BUTTON_SIZE = (50, 50)

play_img = pygame.transform.scale(play_img, BUTTON_SIZE)
stop_img = pygame.transform.scale(stop_img, BUTTON_SIZE)
next_img = pygame.transform.scale(next_img, BUTTON_SIZE)
prev_img = pygame.transform.scale(prev_img, BUTTON_SIZE)

play_rect = play_img.get_rect(center=(125, 250))
stop_rect = stop_img.get_rect(center=(250, 250))
next_rect = next_img.get_rect(center=(375, 250))
prev_rect = prev_img.get_rect(center=(50, 250))

def play_music():
    global is_playing, is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        is_paused = False
        print("▶️ Resumed music")
    else:
        pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[current_song_index]))
        pygame.mixer.music.play()
        is_playing = True
        print(f"🎶 Now playing: {songs[current_song_index]}")

def stop_music():
    global is_playing, is_paused
    pygame.mixer.music.pause()
    is_paused = True
    is_playing = False
    print("⏸️ Music paused")

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    play_music()

def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    play_music()

play_music()

running = True
while running:
    screen.fill((30, 30, 30))
    
    screen.blit(play_img, play_rect)
    screen.blit(stop_img, stop_rect)
    screen.blit(next_img, next_rect)
    screen.blit(prev_img, prev_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                previous_song()
            elif event.key == pygame.K_s:
                stop_music()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if play_rect.collidepoint(mouse_pos):
                play_music()
            elif stop_rect.collidepoint(mouse_pos):
                stop_music()
            elif next_rect.collidepoint(mouse_pos):
                next_song()
            elif prev_rect.collidepoint(mouse_pos):
                previous_song()

    pygame.display.flip()

pygame.quit()