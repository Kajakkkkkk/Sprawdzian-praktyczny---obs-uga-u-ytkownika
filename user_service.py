users = []
user_id_counter = 1


class UserService:
    @staticmethod
    def get_user_by_id(user_id):
        for user in users:
            if user['id'] == user_id:
                return user
        return None

    @staticmethod
    def validate_user_data(user_data):
        valid_groups = ["user", "premium", "admin"]
        if not all(key in user_data for key in ['firstName', 'lastName', 'birthYear', 'group']):
            return False
        if not isinstance(user_data['birthYear'], int) or user_data['birthYear'] <= 0:
            return False
        if user_data['group'] not in valid_groups:
            return False
        return True

    @staticmethod
    def create_user(user_data):
        global user_id_counter
        if UserService.validate_user_data(user_data):
            user_data['id'] = user_id_counter
            users.append(user_data)
            user_id_counter += 1
            return user_data['id']
        return None

    @staticmethod
    def update_user(user_id, user_data):
        if UserService.get_user_by_id(user_id):
            if UserService.validate_user_data(user_data):
                for user in users:
                    if user['id'] == user_id:
                        user.update(user_data)
                        return True
        return False

    @staticmethod
    def delete_user(user_id):
        for user in users:
            if user['id'] == user_id:
                users.remove(user)
                return True
        return False
