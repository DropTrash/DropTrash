# Variáveis que podem ser alteradas durante o jogo
# e precisam ser acessadas por diferentes módulos de cena.

# Cenas
current_scene_name = "home"
control_mike_scenes = 1  # Para a sequência de cenas do Mike

# Itens do Jogo e Dragging
trash_items = []
garbage_bins = []
dragging_item = None
mouse_offset_x = 0
mouse_offset_y = 0

# Status do Nível
level_completed = False
current_lifes = 0  # Será inicializado em setup_gaming_scene
