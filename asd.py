if level[(self.y_pos - 16) // num1][self.x_pos // num2] == 9:
    self.turns[2] = True
if level[self.y_pos // num1][(self.x_pos - num3) // num2] != 8 \
        or (level[self.y_pos // num1][(self.x_pos - num3) // num2] == 9 and (
        self.in_box or self.dead)):
    self.turns[1] = True
if level[self.y_pos // num1][(self.x_pos + num3) // num2] != 8 \
        or (level[self.y_pos // num1][(self.x_pos + num3) // num2] == 9 and (
        self.in_box or self.dead)):
    self.turns[0] = True
if level[(self.y_pos + num3) // num1][self.x_pos // num2] != 8 \
        or (level[(self.y_pos + num3) // num1][self.x_pos // num2] == 9 and (
        self.in_box or self.dead)):
    self.turns[3] = True
if level[(self.y_pos - num3) // num1][self.x_pos // num2] != 8 \
        or (level[(self.y_pos - num3) // num1][self.x_pos // num2] == 9 and (
        self.in_box or self.dead)):
    self.turns[2] = True

# Kolizja y
if self.direction == 2 or self.direction == 3:
    if self.x_pos % num2 == 0:
        if level[(self.y_pos + num3) // num1][self.x_pos // num2] != 8 \
                or (level[(self.y_pos + num3) // num1][self.x_pos // num2] == 9 and (
                self.in_box or self.dead)):
            self.turns[3] = True
        if level[(self.y_pos - num3) // num1][self.x_pos // num2] != 8 \
                or (level[(self.y_pos - num3) // num1][self.x_pos // num2] == 9 and (
                self.in_box or self.dead)):
            self.turns[2] = True
    if self.y_pos % num1 == 0:
        if level[self.y_pos // num1][(self.x_pos - num2) // num2] != 8 \
                or (level[self.y_pos // num1][(self.x_pos - num2) // num2] == 9 and (
                self.in_box or self.dead)):
            self.turns[1] = True
        if level[self.y_pos // num1][(self.x_pos + num2) // num2] != 8 \
                or (level[self.y_pos // num1][(self.x_pos + num2) // num2] == 9 and (
                self.in_box or self.dead)):
            self.turns[0] = True

# Kolizja x
if self.direction == 0 or self.direction == 1:
    if self.x_pos % num2 == 0:
        if level[((self.y_pos) // num1) - 1][self.x_pos // num2] != 8 \
                or (level[(self.y_pos + num3) // num1][self.x_pos // num2] == 9 and (
                self.in_box or self.dead)):
            self.turns[3] = True
        if level[((self.y_pos) // num1) - 1][self.x_pos // num2] != 8 \
                or (level[(self.y_pos - num3) // num1][self.x_pos // num2] == 9 and (
                self.in_box or self.dead)):
            self.turns[2] = True
    if self.y_pos % num1 == 0:
        if level[self.y_pos // num1][(self.x_pos - num3) // num2] != 8 \
                or (level[self.y_pos // num1][(self.x_pos - num3) // num2] == 9 and (
                self.in_box or self.dead)):
            self.turns[1] = True
        if level[self.y_pos // num1][(self.x_pos + num3) // num2] != 8 \
                or (level[self.y_pos // num1][(self.x_pos + num3) // num2] == 9 and (
                self.in_box or self.dead)):
            self.turns[0] = True