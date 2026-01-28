# Mapping Logic
# This module defines the mapping between parts, PWM boards and their corresponding GPIO pins.

# Board 1 (0x40): connecting to parts eye and eyebrow
# Board 2 (0x41): connecting to part mouth
# Board 3 (0x42): connecting to part neck and tendon-driven servos

# Pattern: 'function_name': (board_address, pin_number)
# Board ID: 0=0x41, 1=0x40, 2=0x42

MOTOR_MAP = {
    #eyebrow_rigid
    'eyebrow_left_inner': (0,0),

    #eye_rigid
    
    
    #mouth_rigid
    
    
    #neck_rigid
    
    
    #nose_tendon
    
    #cheek_tendon

}