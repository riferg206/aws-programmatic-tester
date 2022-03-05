from yaspin import yaspin


def duration_spinner(func):
    spinner = yaspin(text="Processing request...", color="cyan", timer=True)
    spinner.start()
