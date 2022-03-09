import pygame

pygame.init()

width, height = 400, 400

white = (255, 255, 255)
black = (0, 0, 0)
gray = (70, 70, 70)

screen = pygame.display.set_mode((width, height))
screen.fill((0, 0, 0))
coords = []


def draw_grid():
    for i in range(20):
        pygame.draw.line(screen, gray, (0, 20 * i), (width, 20 * i), 1)
        pygame.draw.line(screen, gray, (20 * i, 0), (20 * i, height), 1)


def give_pos(pos):
    x = 0
    y = 0
    for i in range(21):
        if ((abs(pos[0] - ((i * 20)))) <= 20):
            x = (i - 1) * 20 + 1
        if ((abs(pos[1] - ((i * 20)))) <= 20):
            y = (i - 1) * 20 + 1
    return x, y


def add_tuple(cord_1, cord_2):
    new_cord = (cord_1[0] + cord_2[0], cord_1[1] + cord_2[1])
    return new_cord


def update_squares():
    global coords
    next_generation = []
    for i in coords:
        count = 0
        if (tuple(add_tuple(i, (-20, -20))) in coords):
            count += 1
        if (tuple(add_tuple(i, (0, -20))) in coords):
            count += 1
        if (tuple(add_tuple(i, (20, -20))) in coords):
            count += 1
        if (tuple(add_tuple(i, (-20, 0))) in coords):
            count += 1
        if (tuple(add_tuple(i, (20, 0))) in coords):
            count += 1
        if (tuple(add_tuple(i, (-20, 20))) in coords):
            count += 1
        if (tuple(add_tuple(i, (0, 20))) in coords):
            count += 1
        if (tuple(add_tuple(i, (20, 20))) in coords):
            count += 1
        if (count == 2 or count == 3):
            next_generation.append(i)
    for i in range(21):
        for j in range(21):
            if ((20 * i + 1, 20 * j + 1) not in coords):
                count = 0
                if (tuple(add_tuple((20 * i + 1, 20 * j + 1), (-20, -20))) in coords):
                    count += 1
                if (tuple(add_tuple((20 * i + 1, 20 * j + 1), (0, -20))) in coords):
                    count += 1
                if (tuple(add_tuple((20 * i + 1, 20 * j + 1), (20, -20))) in coords):
                    count += 1
                if (tuple(add_tuple((20 * i + 1, 20 * j + 1), (-20, 0))) in coords):
                    count += 1
                if (tuple(add_tuple((20 * i + 1, 20 * j + 1), (20, 0))) in coords):
                    count += 1
                if (tuple(add_tuple((20 * i + 1, 20 * j + 1), (-20, 20))) in coords):
                    count += 1
                if (tuple(add_tuple((20 * i + 1, 20 * j + 1), (0, 20))) in coords):
                    count += 1
                if (tuple(add_tuple((20 * i + 1, 20 * j + 1), (20, 20))) in coords):
                    count += 1
                if (count == 3):
                    next_generation.append((20 * i + 1, 20 * j + 1))

    screen.fill(black)
    coords = next_generation
    for i in next_generation:
        pygame.draw.rect(screen, white, [i[0], i[1], 19, 19])


def main():
    active = True
    while active:
        # update each frame

        draw_grid()

        pygame.display.update()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                active = False
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                new_pos = give_pos(pygame.mouse.get_pos())

                if (new_pos not in coords):
                    pygame.draw.rect(screen, white, [int(new_pos[0]), int(new_pos[1]), 19, 19])
                    coords.append(new_pos)
                else:
                    pygame.draw.rect(screen, black, [int(new_pos[0]), int(new_pos[1]), 19, 19])
                    coords.remove(new_pos)
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_SPACE):
                    update_squares()


main()
