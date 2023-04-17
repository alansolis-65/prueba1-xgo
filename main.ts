input.onButtonPressed(Button.A, function on_button_pressed_a() {
    xgo.translational_step_continue(xgo.translation_direction_enum.Forward, 25, 1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    xgo.translational_step_continue(xgo.translation_direction_enum.right_shift, 12, 1)
})
PlanetX_AILens.initModule()
PlanetX_AILens.switchfunc(PlanetX_AILens.FuncList.Card)
xgo.init_xgo_serial(SerialPin.P2, SerialPin.P1)
xgo.execution_action(xgo.action_enum.Stand)
basic.forever(function on_forever() {
    if (PlanetX_AILens.trafficCard(PlanetX_AILens.trafficCards.forward)) {
        xgo.translational_step_continue(xgo.translation_direction_enum.Forward, 25, 1)
    }
    
})
