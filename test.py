
vehicle.add_message_listener('RAW_IMU', listenerV)
vehicle.location.global_relative_frame.alt
vehicle.location.global_relative_frame.lat
vehicle.location.global_relative_frame.lon
vehicle.attitude.pitch
def listenerV(self, name, message):
    # Drone.message_log = str(message) 
    # print(str(message))

    if 'RAW_IMU' in message.get_type():
        yacc_value = extract_yacc_value(message)
        global yacc
        yacc = yacc_value
        # print(f"yacc_value : {yacc_value}")


def extract_yacc_value( message):
        # Extract the value of servo3_raw using regular expression
        match = re.search(r'yacc : (-?\d+)', str(message))
        if match:
            return int(match.group(1))
        else:
            return 0