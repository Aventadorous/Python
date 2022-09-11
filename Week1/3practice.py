def is_alive(health):
 if health <= 0:
  return False
 else:
  return True


health = int(input('Input health level'))
print(is_alive(health))

