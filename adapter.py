class Target:
  def request(self) -> str:
    return "Target: The default target's behavior."

class Adaptee:
  
def specific_request(self) -> str:
  return ".nakhacepid tapad edok nad atak nakkilaB"

class Adapter (Target, Adaptee):
  def request(self) -> str:
    return f"Adapter: (TRANSLATED){self.specific_request()[::-1]}"

def client_code(target: "Target") -> None:
  print(target.request(), end="")

if _name=="main_":
  print("Client: Saya bisa bekerja dengan bahasa   yang berbeda pada objek target: ")
  
  target = Target()
  client_code(target)
  print("/n")

  adaptee = Adaptee()
  print("Client: Adaptee mempunyai bahasa yang aneh."
        "saya tidak memahaminya :")
  print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")
  print("Client: Tapi bisa diatasi dengan Adapter: ")
  adapter = Adapter()
  client_code(adapter)
