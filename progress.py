import curses, sys

W = 6  # width of each piece


def app(s, n):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    done, cur = [False] * n, 0
    while True:
        s.erase()
        d = sum(done)
        s.addstr(1, 2, f"Progress: {d * 100 // n}%  ({d}/{n})", curses.A_BOLD)
        for i in range(n):
            x = 2 + i * (W + 1)
            txt = str(i + 1).center(W)
            s.addstr(
                3,
                x,
                txt,
                curses.color_pair(1) if done[i] else curses.A_DIM | curses.A_REVERSE,
            )
            if i == cur:
                s.addstr(4, x, "▲".center(W))
        s.addstr(
            6,
            2,
            "←/→ move   space/enter toggle   1-9 toggle piece   r reset   q quit",
            curses.A_DIM,
        )
        k = s.getch()
        if k in (ord("q"), 27):
            break
        elif k == curses.KEY_LEFT:
            cur = (cur - 1) % n
        elif k == curses.KEY_RIGHT:
            cur = (cur + 1) % n
        elif k in (32, 10):
            done[cur] = not done[cur]
        elif k == ord("r"):
            done = [False] * n
        elif ord("1") <= k <= ord("9") and k - 49 < n:
            cur = k - 49
            done[cur] = not done[cur]


n = int(sys.argv[1]) if len(sys.argv) > 1 else int(input("How many titles? "))
curses.wrapper(app, max(1, n))
