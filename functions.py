from DatabaseConnection import *


class CareAll:
    def __init__(self):
        pass

    @staticmethod
    def RegisterOldies():
        OldieName = input("Enter the name of the elder")
        Fund = input("Enter the fund given by the elder to our Authority")
        Availability = input("Is the Elder available to be taken care by our Young Folk?Enter 0 for NO and 1 for YES ")
        RegisterOldiesDictionary = {"Name": OldieName, "Fund": Fund, "Availability": Availability, "Rating": "",
                                    "Review": "", "Taken Care By": "", "Consent_list": []}
        Elders_Table.insert_one(RegisterOldiesDictionary)

    @staticmethod
    def RegisterYoungFolks():
        YoungsterName = input("Enter the name of the elder")
        Uid = input("Enter your Aadhar Number")
        RegisterYoungFolksDictionary = {"Name": YoungsterName, "UID": Uid, "Rating": "", "Review": "",
                                        "Taking Care of": []}

        YoungFolks_Table.insert_one(RegisterYoungFolksDictionary)

    @staticmethod
    def RatingandReviewOfElders():
        Youngfolkname = input("Please Enter your name")
        ElderName = input("Enter the name of the care taker person")
        rating = input(f"Out of five stars how many stars would you like to give to {ElderName}")
        review = input(f"Please write down your review for {ElderName}")
        print(f"Thank You {Youngfolkname} for your rating and review . Your name will be confidential.Your Feedback is "
              f"important for us")
        Elders_Table.update_one({"Name": ElderName}, {"$set": {"Rating": rating, "Review": review}})

    @staticmethod
    def RatingAndReviewOfYoungFolks():
        ElderName = input("Please Enter your name")
        Youngfolkname = input("Enter the name of the Young person")
        rating = input(f"Out of five stars how many stars would you like to give to {Youngfolkname}")
        review = input(f"Please write down your review for {Youngfolkname}")
        print(f"Thank You {ElderName} for your rating and review .Your Feedback is important for us")
        YoungFolks_Table.update_one({"Name": Youngfolkname}, {"$set": {"Rating": rating, "Review": review}})

    @staticmethod
    def oldies_available():
        cursor = Elders_Table.find({"Availability": 1}, {"Name": 1, "_id": 0})
        if cursor is not None:
            for names in cursor:
                print(names)
        else:
            print("All elders are occupied")

    @staticmethod
    def taken_care_by():
        old_person_name = input("Enter the name of the Elder")
        cursor = Elders_Table.find_one({"Name": old_person_name}, {"Taken Care By": 1})
        array = cursor["Taken Care By"]
        print(f"{old_person_name} is taken care by {array}")

    @staticmethod
    def taking_care():
        young_person_name = input("Enter the name of the Young Folk")
        cursor = YoungFolks_Table.find_one({"Name": young_person_name}, {"Taking Care of": 1})
        array = cursor["Taking Care of"]
        print(f"{young_person_name} is looking after {array}")

    @staticmethod
    def young_making_request():
        # careallobj.taking_care()
        name = input("Enter the name of the young folk")
        cursor = YoungFolks_Table.find_one({"Name": name}, {"Taking Care of": 1})
        array = cursor["Taking Care of"]
        print(f"{name} is looking after {array}")
        print(len(array))
        if len(array) < 4:
            print("You are eligible. Go on for this good deed")
            request_old = input("Enter the name of the elder who is to be looked after")
            return name, request_old
        else:
            print("You already are taking care of 4 elders")
            return "none", "none"

    @staticmethod
    def checking_eligiblity_of_Young_Folk():
        requested_by, requested_for = (CareAllObj.young_making_request())
        if requested_by == "none":
            return
        # print(requested_by, requested_for)
        cursor = Elders_Table.find_one({"Name": requested_for}, {"_id": 0, "Availability": 1})
        array = cursor["Availability"]
        # print(array)
        if array == 0:
            print(f'Sorry {requested_for} is not available')
        elif array == 1:
            print(f'{requested_for} is available but we need to take consent from {requested_for}')
            cursor = Elders_Table.find_one({"Name": requested_for}, {"_id": 0, "Consent_list": 1})
            array = cursor["Consent_list"]
            # print(array)
            updated_list = []
            for i in array:
                # print(i)
                updated_list.append(i)
            updated_list.append(requested_by)
            print(updated_list)
            Elders_Table.update_one({"Name": requested_for}, {"$set": {"Consent_list": updated_list}})

    @staticmethod
    def approval_by_old_person():
        ElderName = input("Enter the name whose Consent List is to be checked")
        cursor = Elders_Table.find_one({"Name": ElderName}, {"_id": 0, "Consent_list": 1})
        array = cursor["Consent_list"]
        print(array)
        consent = input("Give your Consent to any of the above present in the list")
        Elders_Table.update_one({"Name": ElderName}, {"$set": {"Taken Care By": consent}})
        Elders_Table.update_one({"Name": ElderName}, {"$set": {"Consent_list": []}})
        Elders_Table.update_one({"Name": ElderName}, {"$set": {"Availability": 0}})

    @staticmethod
    def showElder_details():
        ElderName = input("Enter the name of the Elder whose detail is needed")
        cursor = Elders_Table.find_one({"Name": ElderName})
        for eldername in cursor:
            print(eldername, " : ", cursor[eldername])

    @staticmethod
    def showYoung_details():
        ElderName = input("Enter the name of the Young folk whose detail is needed")
        cursor = YoungFolks_Table.find_one({"Name": ElderName})
        for eldername in cursor:
            print(eldername, " : ", cursor[eldername])


CareAllObj = CareAll()
# CareAllObj.checking_eligiblity_of_Young_Folk()

# function to find out all the people being currently taken care
def all_people_being_taken_care():
    # YoungFolks_Table.insert_many(YoungFolks_List)
    # Elders_Table.insert_many(Elders_Table_List)
    cursor = Elders_Table.find({"Availability": 0}, {"_id": 0, "Name": 1, "Taken Care By": 1})
    elder_list = []
    for value in cursor:
        elder_list.append(value)
    return elder_list

# print(all_people_being_taken_care())


# function to find out a given young person is taking care of how many people
def young_person_taking_care_of(name):
    cursor = YoungFolks_Table.find({"name": name}, {"_id": 0, "Name": 1, "Taking Care Of": 1})
    younger_list = []
    for value in cursor:
        younger_list.append(value)
    return younger_list
