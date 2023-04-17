def on_button_pressed_a():
    xgo.translational_step_continue(xgo.translation_direction_enum.FORWARD, 25, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    xgo.translational_step_continue(xgo.translation_direction_enum.RIGHT_SHIFT, 12, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

PlanetX_AILens.init_module()
PlanetX_AILens.switchfunc(PlanetX_AILens.FuncList.CARD)
xgo.init_xgo_serial(SerialPin.P2, SerialPin.P1)
xgo.execution_action(xgo.action_enum.STAND)

def on_forever():
    if PlanetX_AILens.traffic_card(PlanetX_AILens.trafficCards.FORWARD):
        xgo.translational_step_continue(xgo.translation_direction_enum.FORWARD, 25, 1)
basic.forever(on_forever)
