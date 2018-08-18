class User(object):
    current_id = 0
    users = []

    def create(self, username, email, password):
        self.current_id +=1
        new_user = {
            'id': self.current_id,
            'username': username,
            'email': email,
            'password': password,
        }

        self.users.append(new_user)

        return self.users
