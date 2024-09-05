

class Account():

    def __init__(self) -> None:
        pass

    def create_account_username_password(self, parse_username, parse_password, parse_repassword):

        username = parse_username
        password = parse_password
        retype_password = parse_repassword

        if password == retype_password:
            with open("accounts.txt", "w") as file:
                file.write(username, password)
            return True

        else:
            return False
        
    def create_account_data(self):
        full_name = input("Enter Full Name: ")
        job = input("Masukkan Pekerjaan: ")
        salary = input("Masukkan Gaji: ")
        job_address = input("Masukkan Alamat Pekerjaan: ")
        tanggungan = input("Masukkan Jumlah Tanggungan: ")
        beban_cicilan = input("Masukkan Beban Cicilan: ")
        tabungan = input("Masukkan Tabungan: ")

        with open("accounts.txt", "w") as file:
            file.write(full_name, job, salary, job_address, tanggungan, beban_cicilan, tabungan)
        
        is_saved = 1
        return is_saved
    
    def user_login(self, parsed_username, parsed_password):
        username = parsed_username
        password = parsed_password
        with open("accounts.txt", "r") as file:
            for line in file:
                if username in line and password in line:
                    return True
                else:
                    return False
            
        