let number = 0
let num2 = 0
input.onButtonPressed(Button.A, function () {
    basic.showNumber(number)
})
input.onButtonPressed(Button.AB, function () {
    if (number > num2) {
        basic.showLeds(`
            # . . . .
            . # . . .
            . . # . .
            . # . . .
            # . . . .
            `)
    } else if (number == num2) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . . . . .
            . # # # .
            . . . . .
            `)
    } else {
        basic.showLeds(`
            . . . . #
            . . . # .
            . . # . .
            . . . # .
            . . . . #
            `)
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(num2)
})
input.onGesture(Gesture.Shake, function () {
    num2 = randint(0, 10)
    number = randint(0, 10)
})
basic.forever(function () {
	
})
