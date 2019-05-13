#! usr/bin/env python3
# coding=utf8


class Globals:

    width, height = None, None
    pillars = {0: [], 1: [], 2: [], 3: [], 4: []}

    num_moves = 0

    @staticmethod
    def reset_pillars():
        Globals.pillars = {0: [], 1: [], 2: [], 3: [], 4: []}

    @staticmethod
    def reset_moves():
        Globals.num_moves = 0

    @staticmethod
    def reset():
        Globals.reset_pillars()
        Globals.reset_moves()


def unpack(position, dests):
    if dests and Globals.pillars[position]:
        dest = dests.pop(0)
        if dest == position:
            return
        Globals.pillars[dest].append(Globals.pillars[position].pop())
        draw_disks(Globals.pillars, Globals.height)
        Globals.num_moves += 1
        assert Globals.pillars[position] == sorted(Globals.pillars[position], reverse=True)
        unpack(position, dests)


def repack(positions, dest):
    if positions:
        position = positions.pop()
        if Globals.pillars[position]:
            Globals.pillars[dest].append(Globals.pillars[position].pop())
            draw_disks(Globals.pillars, Globals.height)
            Globals.num_moves += 1
            assert Globals.pillars[dest] == sorted(Globals.pillars[dest], reverse=True)
            repack(positions, dest)


def move_less_than_4(disks, source, target, auxillary):
    if disks > 0:
        move_less_than_4(disks - 1, source, auxillary, target)
        Globals.pillars[target].append(Globals.pillars[source].pop())
        draw_disks(Globals.pillars, Globals.height)
        move_less_than_4(disks - 1, auxillary, target, source)


def center_move(occupied, last_center):
    occupied.sort()
    dest = occupied[-1]
    dests = []
    for i in range(5):
        if (i > occupied[1] or i == last_center) and i != dest:
            dests.append(i)
    unpack(occupied[1], list(dests))
    repack(dests + [occupied[1]], dest)
    dests = []
    for i in range(5):
        if (i > occupied[0] or i == last_center) and i != dest:
            dests.append(i)
    unpack(occupied[0], list(dests))
    repack(dests + [occupied[0]], dest)
    return occupied[2:]


def finish_move(occupied, finalize):
    if finalize and Globals.pillars[4]:
        occupied.pop()
        if not occupied:
            return
    occupied.sort()
    position = occupied.pop()
    if len(Globals.pillars[position]) == 1:
        repack([position], 4)
        finish_move(occupied, False)
    else:
        positions = []
        for i in range(4):
            if not Globals.pillars[i]:
                positions.append(i)
        unpack(position, list(positions))
        repack(positions + [position], 4)
        if occupied:
            finish_move(occupied, False)


def move(disks, occupied, nums, center=(0, 0), finalize=False):
    if disks < 4 and nums == 0:
        move_less_than_4(disks, 0, 4, 3)
    elif Globals.pillars[center[1]] and (
            len(occupied) != 3 or len(Globals.pillars[center[1]]) == 1
        ):
        rang = (
            range(4, -1, -1) if nums % 2 == 0 or disks > 7 else range(0, 5, 1)
        )
        positions = []
        length = len(Globals.pillars[center[1]])
        for i in rang:
            if not Globals.pillars[i] or (
                    i == 4 and len(Globals.pillars[center[1]]) != 2
                ):
                positions.append(i)
        if len(positions) < 4:
            positions.append(center[1])
        unpack(center[1], list(positions))
        if length > 1:
            if positions[-1] == center[1]:
                if not positions[:-1]:
                    repack(positions, 4)
                else:
                    repack(positions[:-2], positions[:-1].pop())
            else:
                repack(positions, positions.pop())
        move(
            8 if center[0] == 3 else disks,
            []
            if center[0] != center[1]
            else occupied + [(nums) % 4]
            if nums > 3
            else occupied + [(nums + 1) % 4],
            nums + 1,
            center=(center[0], center[0]),
            finalize=not Globals.pillars[center[0]],
        )
    elif len(occupied) == 3 and Globals.pillars[center[1]]:
        occupied = center_move(occupied, center[1])
        move(disks - 9, occupied, nums, center=(occupied[0], center[1]))
    elif occupied:
        finish_move(occupied, finalize or len(occupied) > 3)


def draw_disks(pillars, position):
    if position >= 0:
        pillar_values = {}
        for i in range(5):
            pillar_values[i] = (
                " "
                if position >= len(pillars[i])
                else create_disk(pillars[i][position])
            )
        print(
            "{0:^{width}}{1:^{width}}{2:^{width}}{3:^{width}}{4:^{width}}".format(
                pillar_values[0],
                pillar_values[1],
                pillar_values[2],
                pillar_values[3],
                pillar_values[4],
                width=Globals.width,
            )
        )
        draw_disks(pillars, position - 1)
    else:
        print(
            "{0:^{width}}{1:^{width}}{2:^{width}}{3:^{width}}{4:^{width}}\n".format(
                "A", "B", "C", "D", "E", width=Globals.width
            )
        )


def create_disk(size):
    return ("/" * size) + ("\\" * size)


def input_int(prompt, min_input=None, max_input=None):
    """

    """
    while True:
        val = None
        try:
            val = int(input(prompt))
            if min_input is not None and val < min_input:
                print(f'The value "{val}" is too small, it can be at least {min_input}')
                continue
            if max_input is not None and val > max_input:
                print(f"The value {val} is too large, it can be at most {max_input}.")
                continue
            return val
        except ValueError:
            print(f'The value "{val}" is not an integer.')


def main(disks=None):
    disks = disks if disks is not None else input_int("Please enter the number of disks: ", min_input=1, max_input=30)

    Globals.pillars[0] = [i for i in range(disks, 0, -1)]
    Globals.width = 2 * disks
    Globals.height = disks - 1

    moves = 2 ** disks - 1
    five_peg_moves = [1, 3, 7, 14, 16, 18, 19, 25, 30, 31, 58, 59]
    five_peg_moves_optimal = [1, 3, 5, 7, 11, 17, 18, 25, "9 disks", "10 disks", "11 disks", "12 disks"]
    word = "moves" if moves > 1 else "move"
    print(f"\nWith {disks} disks a perfect game will require {moves} {word}. \n")

    print("Starting Configuration:")
    draw_disks(Globals.pillars, Globals.height)

    move(disks, [], 0)
    return moves if disks < 4 else Globals.num_moves


if __name__ == "__main__":
    main()
    #moves = []
    #for i in range(1, 13, 1):
    #    moves.append(main(i))
    #    Globals.reset()
    #print(moves)

    """
    Tested optimizations up to 8. Values 3-6 not fully optimized
        for 5 pegs(optimized values found below). They are
        however tested to never place a bigger piece on a smaller piece.

    Globals.reset()
    assert main(1) == 1
    Globals.reset()
    assert main(2) == 3
    Globals.reset()
    assert main(3) == 7
    Globals.reset()
    assert main(4) == 14
    Globals.reset()
    assert main(5) == 16
    Globals.reset()
    assert main(6) == 18
    Globals.reset()
    assert main(7) == 19
    Globals.reset()
    assert main(8) == 25
    """

    """ 5 Disks-11
    0 -> 4
    0 -> 3
    0 -> 2
    0 -> 1
    4 -> 1
    0 -> 4
    1 -> 0
    1 -> 4
    2 -> 4
    3 -> 4
    0 -> 4
    """
    """ 6 Disks-17
    Unpack initial
    0 -> 4
    0 -> 3
    0 -> 2
    0 -> 1
    Repack initial
    2 -> 1
    3 -> 1
    4 -> 1
    Unpack secondary
    0 -> 3
    0 -> 4
    Repack secondary
    3 -> 4
    Unpack initial again
    1 -> 0
    1 -> 2
    1 -> 3
    Finalize/Repack
    1 -> 4
    3 -> 4
    2 -> 4
    0 -> 4
    """
    """ 7 Disks-19
    Unpack initial
    0 -> 4
    0 -> 3
    0 -> 2
    0 -> 1
    Repack initial
    2 -> 1
    3 -> 1
    4 -> 1
    Unpack secondary
    0 -> 2
    0 -> 3
    0 -> 4
    Repack secondary
    3 -> 4
    2 -> 4
    Unpack initial again
    1 -> 0
    1 -> 2
    1 -> 3
    Finalize/Repack
    1 -> 4
    3 -> 4
    2 -> 4
    0 -> 4
    """
    """ 8 Disks-25
    Unpack initial
    0 -> 4
    0 -> 3
    0 -> 2
    0 -> 1
    Repack initial
    2 -> 1
    3 -> 1
    4 -> 1
    Unpack secondary
    0 -> 4
    0 -> 3
    0 -> 2
    Repack secondary
    4 -> 2
    3 -> 2
    Unpack tertiary
    0 -> 4
    Unpack Secondary
    2 -> 0
    2 -> 3
    Finalize/Repack secondary
    2 -> 4
    3 -> 4
    0 -> 4
    Unpack initial
    1 -> 0
    1 -> 2
    1 -> 3
    Finalize/Repack
    1 -> 4
    3 -> 4
    2 -> 4
    0 -> 4
    """
