
import serial


ser = serial.Serial('COM3', 9600)  # Replace with the appropriate serial port and baud rate

command = "spin_spindel\n"  # Replace with the appropriate command

ser.write(command.encode())
ser.close()

print("OK")




import avend_machine_library
print("avend_machine_library")
