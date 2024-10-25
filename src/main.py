import time
import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('RPG Game')
		self.clock = pygame.time.Clock()

		self.level = Level()

		# sound 
		main_sound = pygame.mixer.Sound('audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)

	def show_start_screen(self):
		self.screen.fill((0, 0, 0))

		BACKGROUND_COLOR = (30, 30, 30)
		TITLE_COLOR = (173, 216, 230)  # Azul claro
		INSTRUCTION_COLOR = (144, 238, 144)  # Verde claro
			
		# Definir fontes e textos
		title_font = pygame.font.Font(None, 100)
		instruction_font = pygame.font.Font(None, 40)

		title_text = title_font.render("RPG Game", True, TITLE_COLOR)
		instruction_text = instruction_font.render("Press ENTER to start", True, INSTRUCTION_COLOR)

		# Calcular a posição centralizada
		title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGTH // 2 - 100))
		instruction_rect = instruction_text.get_rect(center=(WIDTH // 2, HEIGTH // 2 + 150))

			# Controle de animação de piscar
		blink = True
		waiting = True
		last_blink_time = time.time()

		while waiting:
			self.screen.fill(BACKGROUND_COLOR)

			# Exibir título com sombra
			shadow_offset = 2
			shadow_color = (0, 0, 0)  # Cor da sombra
			title_shadow = title_font.render("RPG Game", True, shadow_color)
			self.screen.blit(title_shadow, (title_rect.x + shadow_offset, title_rect.y + shadow_offset))
			self.screen.blit(title_text, title_rect)
				
			# Piscar o texto de instrução
			if blink:
				instruction_shadow = instruction_font.render("Press ENTER to start", True, shadow_color)
				self.screen.blit(instruction_shadow, (instruction_rect.x + shadow_offset, instruction_rect.y + shadow_offset))
				self.screen.blit(instruction_text, instruction_rect)

			pygame.display.flip()

				# Gerenciamento de eventos
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						waiting = False

			# Alterna o estado de piscar a cada 0.5 segundos
			if time.time() - last_blink_time > 0.5:
				blink = not blink
				last_blink_time = time.time()
    
	def run(self):
		game.show_start_screen()
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()