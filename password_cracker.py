import hashlib

def crack_sha1_hash(hash, use_salts = False):
    if use_salts:
        try:
            with open('top-10000-passwords.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    password = line.strip()
                    with open('known-salts.txt', 'r', encoding='utf-8') as salts:
                        for s in salts:
                            salt = s.strip()
                            combined_data = (salt+password).encode('utf-8')
                            hash_object = hashlib.sha1(combined_data)
                            hash_result = hash_object.hexdigest()
                            if hash_result == hash:
                                return password
                else:
                     return 'PASSWORD NOT IN DATABASE'
        except FileNotFoundError:
            print("指定的文件不存在，请检查文件路径和名称是否正确")
    else:
        try:
            with open('top-10000-passwords.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    password = line.strip()
                    hash_object = hashlib.sha1(password.encode('utf-8'))
                    hash_result = hash_object.hexdigest()
                    if hash_result == hash:
                        return password
                else:
                    return 'PASSWORD NOT IN DATABASE'
        except FileNotFoundError:
            print("指定的文件不存在，请检查文件路径和名称是否正确")
    return True