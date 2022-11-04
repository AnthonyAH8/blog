from datetime import date
from .config import configdb
import mysql.connector

class Contact:

    # Constructeur
    def __init__(self, id, firstname, lastname, birth_date, phone, email): 
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birth_date = birth_date
        self.phone = phone
        self.email = email

    # Permet de retourner l'age comme un attribut de l'objet
    @property
    def full_name(self): 
        return f'{self.firstname[:1].upper()}{self.firstname[1:].lower()} {self.lastname.upper()}'

    # La soustraction est un booléen qui retourne 0 ou 1 selon l'age de la personne
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
        
    def __str__(self): 
        return f"""
        id : {self.id}
        identité : {self.full_name}
        age : {self.age}
        telephone : {self.phone}
        email : {self.email}
        """
    @staticmethod
    def get_all_contacts():

        contacts = []

        with mysql.connector.connect(**configdb) as db: 
            with db.cursor() as cursor:
                query = "SELECT contact_id, firstname, lastname, birth_date, phone, email FROM contact"
                try:
                    cursor.execute(query)
                    results = cursor.fetchall()

                    # Parcours du jeu de résultats pour créer des contacts et les ajouter dans un tableau
                    for id, firstname, lastname, birth_date, phone, email in results:
                        contact = Contact(id, firstname, lastname, birth_date, phone, email)
                        contacts.append(contact)
                
                except Exception as ex:
                    print(ex)
        return contacts