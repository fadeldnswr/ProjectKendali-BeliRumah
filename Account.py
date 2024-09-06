import json
import numpy as np

class Account():

    def __init__(self) -> None:
        pass

    def read_credentials(self):
        with open("accounts_credentials.json", "r") as file:
            accounts_credentials = json.load(file)
            file.seek(0)

            for _ in accounts_credentials:
                if accounts_credentials["unique_id"] == self.id_number:
                    return accounts_credentials["username"]
            

    # Create Account Functions
    def create_account_username_password(self, parse_username, parse_password, parse_repassword):

        self.id_number = np.random.randint(1000, 10000)
        retype_password = parse_repassword

        account_credentials = {
            "username": parse_username,
            "password": parse_password,
            "unique_id": self.id_number
        }

        if account_credentials["password"] == retype_password:
            with open("accounts_credentials.json", "a") as file:
                json.dump(account_credentials, file)
            return True
        
        else:
            return False

    # Create Account Data Functions    
    def create_account_data(self, parse_nama, parse_pekerjaan, parse_email, parse_gaji, parse_tempat_kerja, parse_tanggungan, parse_cicilan, parse_tabungan):
        
        account_data = {
            "unique_id": self.id_number, # Should Identify the Account of an user ideally yeah?
            "full_name": parse_nama,
            "email": parse_email,
            "job": parse_pekerjaan,
            "salary": parse_gaji,
            "job_address": parse_tempat_kerja,
            "tanggungan": parse_tanggungan,
            "beban_cicilan": parse_cicilan,
            "tabungan": parse_tabungan
        }

        with open("accounts_data.json", "a") as file:
            json.dump(account_data, file)
        return True
    
    # Login Functions
    def user_login(self, parsed_username, parsed_password):
        
        username = parsed_username
        password = parsed_password
        with open("accounts_credentials.json", "r") as file:
            credentials = json.load(file)
            if credentials["username"] == username and credentials["password"] == password:
                self.id_number = credentials["unique_id"]
                return True
            else:
                return False
            
    # Changing User Data Functions
    def change_user_data(self, parse_nama, parse_pekerjaan, parse_email, parse_gaji, parse_tempat_kerja, parse_tanggungan, parse_cicilan, parse_tabungan):
        
        account_data = {
            "unique_id": self.id_number, # Should Identify the Account of an user ideally yeah?
            "full_name": parse_nama,
            "email": parse_email,
            "job": parse_pekerjaan,
            "salary": parse_gaji,
            "job_address": parse_tempat_kerja,
            "tanggungan": parse_tanggungan,
            "beban_cicilan": parse_cicilan,
            "tabungan": parse_tabungan
        }

        with open("accounts_data.json", "r+") as file:
            accounts_data = json.load(file)
            file.seek(0)
            
            for account in accounts_data:
                if account["unique_id"] == self.id_number:
                    account.update(account_data)
            
            file.truncate()
            json.dump(accounts_data, file)

        return True
        
    # Ressetting User Password Functions
    def search_user_email(self, parse_email):
        
        with open("accounts_data.json", "r") as file:
            data = json.load(file)
            file.seek(0)
            
            for _ in data:
                if data["email"] == parse_email:
                    return True
            else:
                return False
            
    def reset_user_password(self, parse_password, parse_repassword):
        
        if parse_password == parse_repassword:
            with open("accounts_credentials.json", "r+") as file:
                credentials = json.load(file)
                file.seek(0)
            
                for account in credentials:
                    account["password"] = parse_password
            
                file.truncate()
                json.dump(account, file)
            return True
        else:
            return False