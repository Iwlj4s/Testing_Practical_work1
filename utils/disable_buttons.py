def disable_buttons(*buttons):
    for button in buttons:
        button.setDisabled(True)


def enable_buttons(*buttons):
    for button in buttons:
        button.setDisabled(False)


def open_window_and_enable_buttons(window, *buttons_to_disable):
    window.show()

    def on_window_close_event(event):
        enable_buttons(*buttons_to_disable)

    window.closeEvent = on_window_close_event

