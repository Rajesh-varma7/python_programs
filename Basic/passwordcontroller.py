def password_controller(password):
  if len(password) > 8:
    return True
  else:
    return False
password_controller("abcdefghi")
