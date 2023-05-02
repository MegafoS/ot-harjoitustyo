import pygame
from player_ship import PlayerShip
from enemy_ship import EnemyShip
from player_actions import PlayerActions
from game_values import GameValues
from collision_detection import CollisionDetection
from screen_refresh import refresh_screen
from level_constructor import start_new_level
game_values = GameValues()
collision_detection = CollisionDetection()
screen_size = game_values.screen_size
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(game_values.name)
def main(test_mode = False):
    clock = pygame.time.Clock()
    running = True
    player_ship = PlayerShip((screen_size[0]-52)/2, screen_size[1]-100, 4, 100)
    game_values.level = 1
    enemy_ship = EnemyShip(0, 0, 0, 0)
    player_actions = PlayerActions
    start_new_level(enemy_ship, game_values)
    while running and not test_mode:
        clock.tick(game_values.fps)
        refresh_screen(screen, player_ship, enemy_ship)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player_ship.damage_immunity_update()
        collision_detection.player_and_enemy_collision(player_ship,enemy_ship)
        collision_detection.bullet_and_enemy_collision(player_ship,enemy_ship)
        if player_ship.lives == 0 or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
        player_actions.player_actions(None,player_ship)
        for enemy in enemy_ship.enemies:
            if enemy.y_coord > game_values.screen_size[1]:
                player_ship.lives -=1
                print("enemy through! lives left:", player_ship.lives)
                enemy_ship.enemies.remove(enemy)
        if len(enemy_ship.enemies) == 0:
            game_values.level +=1
            start_new_level(enemy_ship, game_values)
        enemy_ship.enemies_advance()
        player_ship.bullet_list_updater()
if __name__ == "__main__":
    main()
