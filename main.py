import studentregsiter
import studentdetails
import studentsearch

def menu():
    print("\n---Student Registration---")
    print("1 - Register Student")
    print("2 - Get details")
    print("3 - Search Student")
    print("0 - Exit")
 
def userinput():
    data = []
    while True:
        task_input = input("\nEnter task number: ")
        if task_input.isdigit():
            task_input = int(task_input)
            if task_input == 1:
                data = studentregsiter.register_student()
            elif task_input == 2:
                studentdetails.get_student(data)
            elif task_input == 3:
                studentsearch.search_student(data)
            elif task_input == 0:
                break
            else:
                print("Choose Valid option")
        else:
            print("Task number should be in digit")
    
menu()
userinput()