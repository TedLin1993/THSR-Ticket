class ConfirmTicketInfo:
    def __init__(self) -> None:
        pass

    def personal_id_info(self, default_value: str = None, select: bool = True) -> str:
        if select:
            print(f"輸入身分證字號(預設: {default_value}): ")
            return input() or default_value
        print(f"輸入身分證字號: {default_value}")
        return default_value

    def phone_info(self, default_value: str = "", select: bool = True) -> str:
        if select:
            print(f"輸入手機號碼(預設: {default_value}): ")
            return input() or default_value
        print(f"輸入手機號碼: {default_value}")
        return default_value
