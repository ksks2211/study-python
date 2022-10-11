class Tiger:
	def __init__(self) -> None:
		super().__init__()
		print("Tiger Init")

	def Jump(self):
		print("Jump")


class Lion:
	def __init__(self) -> None:
		super().__init__()
		print("Lion Init")

	def Bite(self):
		print("Bite")


class Liger(Tiger, Lion):
	def __init__(self) -> None:
		super().__init__()
		print("Liger INit")

	def Play(self):
		print("Play")


print(Liger.__mro__)

liger = Liger()

liger.Bite()
liger.Jump()
liger.Play()
