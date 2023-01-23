number = 0
num2 = 0

def on_button_pressed_a():
    basic.show_number(number)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if number > num2:
        basic.show_leds("""
            # . . . .
                        . # . . .
                        . . # . .
                        . # . . .
                        # . . . .
        """)
    elif number == num2:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . . . . .
                        . # # # .
                        . . . . .
        """)
    else:
        basic.show_leds("""
            . . . . #
                        . . . # .
                        . . # . .
                        . . . # .
                        . . . . #
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_number(num2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global num2, number
    num2 = randint(0, 10)
    number = randint(0, 10)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
