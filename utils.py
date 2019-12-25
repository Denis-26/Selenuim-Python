from values import Values


class Utils:
    @staticmethod
    def build_shooting_date_str(start, end, delta):
        return Values.START_SHOOTING_DAY + " - " + Values.END_SHOOTING_DAY + " " + "({days_delta} дней)".format(
            days_delta=delta)
