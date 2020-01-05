import test
from functions import *


def run_tests():
    print("Saving the default data and running tests")
    Elders_Table.insert_many(Elders_Table_List)
    YoungFolks_Table.insert_many(YoungFolks_List)
    test_obj = test.MyTestCase()
    test_obj.test_person_taking_care_of_elders()


def Operations():
    while True:

        choice = int(input("Enter the operation You want to perform?\n"
                           "1. Register an Elder\n"
                           "2. Register a Young Folk\n"
                           "3. Give Rating and Review to a Young Folk\n"
                           "4. Give Rating and Review to an Elder\n"
                           "5. List of all the Elders available.\n"
                           "6. To Check an Elderly person is taken care by whom?\n"
                           "7. To know the names of all the Elders a Young Chap is taking care of \n"
                           "8. Make a request as Young Chap and also checking whether he is eligible to make a "
                           "request or not\n "
                           "9. To approve a Young Chap to take care of an elder\n"
                           "10. Show all the details of Young chap\n"
                           "11. Show all the details of an Old Person\n"
                           "12. Exit\n"))

        if choice == 1:
            CareAllObj.RegisterOldies()

        elif choice == 2:
            CareAllObj.RegisterYoungFolks()
        elif choice == 3:
            CareAllObj.RatingandReviewOfElders()

        elif choice == 4:
            CareAllObj.RatingAndReviewOfYoungFolks()
        elif choice == 5:
            CareAllObj.oldies_available()

        elif choice == 6:
            CareAllObj.taken_care_by()
        elif choice == 7:
            CareAllObj.taking_care()

        elif choice == 8:
            CareAllObj.checking_eligiblity_of_Young_Folk()

        elif choice == 9:
            CareAllObj.approval_by_old_person()

        elif choice == 10:
            CareAllObj.showYoung_details()

        elif choice == 11:
            CareAllObj.showElder_details()

        elif choice == 12:
            print("Thank You For giving us time to grow")
            exit(0)


if __name__ == "__main__":
    if "EDYODA_CAREALL" not in client.list_database_names():
        run_tests()
        print(f"All people being taken care {all_people_being_taken_care()}")
        CareAllObj = CareAll()
        Operations()
    else:
        CareAllObj = CareAll()
        Operations()
