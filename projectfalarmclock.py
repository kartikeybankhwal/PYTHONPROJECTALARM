import time
import winsound

def set_alarm_time():
    print("Enter the  KARTIKEY'S alarm time (format: HH:MM)")
    alarm_time = input(">> ")
    return alarm_time

def set_alarm_frequency():
    print("Select alarm frequency:")
    print("1. MODERATE")
    print("2. MEDIAN")
    print("3. IMENSE")
    frequency_choice = input(">> ")
    if frequency_choice == "1":
        alarm_frequency = [500, 1000]  # Low frequency
    elif frequency_choice == "2":
        alarm_frequency = [1000, 2000]  # Medium frequency
    elif frequency_choice == "3":
        alarm_frequency = [2000, 3000]  # High frequency
    return alarm_frequency

def start_alarm(alarm_time, alarm_frequency):
    current_time = time.strftime("%H:%M")
    while current_time != alarm_time:
        current_time = time.strftime("%H:%M")
        time.sleep(1)
    print("Alarm!")
    for freq in alarm_frequency:
        winsound.Beep(freq, 500)  # Beep at each frequency for 500ms

def main():
    while True:
        print("\nMenu:")
        print("1. Set alarm time")
        print("2. Set alarm frequency")
        print("3. Start alarm")
        print("4. Exit")
        choice = input(">> ")

        if choice == "1":
            alarm_time = set_alarm_time()
        elif choice == "2":
            alarm_frequency = set_alarm_frequency()
        elif choice == "3":
            try:
                start_alarm(alarm_time, alarm_frequency)
            except NameError:
                print("Please set alarm time and frequency first!")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
