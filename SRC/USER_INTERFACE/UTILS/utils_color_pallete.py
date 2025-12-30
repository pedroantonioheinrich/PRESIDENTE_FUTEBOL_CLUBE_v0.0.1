class ColorPallete:

    def __init__(self):
        self.RESET = "RESET"
        self.BOLD = "BOLD"
        self.GREEN = "GREEN"
        self.YELLOW = "YELLOW"
        self.RED = "RED"
        self.CYAN = "CYAN"
        self.BLUE = "BLUE"
        self.WHITE = "WHITE"
        self.MAGENTA = "MAGENTA"
        self.GOLDEN = "GOLDEN"
        self.SILVER = "SILVER"
        self.BLACK = "BLACK"


    def color_picker(self, color_name):
        match(color_name):
            case "RESET":
                return "\033[0m"
            case "BOLD":
                return "\033[1m"
            case "GREEN":
                return "\033[1;32m"
            case "YELLOW":
                return "\033[1;33m"
            case "RED":
                return "\033[1;31m"
            case "CYAN":
                return "\033[1;36m"
            case "BLUE":
                return "\033[1;34m"
            case "WHITE":
                return "\033[1;37m"
            case "MAGENTA":
                return "\033[1;35m"
            case "GOLDEN":
                return "\033[38;5;220m"
            case "SILVER":
                return "\033[38;5;250m"
            case "BLACK":
                return "\033[1;30m"
            case _:
                return "\033[0m"