# Mapping Logic
# This module defines the mapping between parts, PWM boards and their corresponding GPIO pins.

# Board 1 (0x40): connecting to parts eye and eyebrow
# Board 2 (0x41): connecting to part mouth
# Board 3 (0x42): connecting to part neck and tendon-driven servos

# Pattern: 'function_name': (board_address, pin_number)
# Board ID: 0=0x41, 1=0x40, 2=0x42

MOTOR_MAP = {
    #eyebrow_rigid
    'eyebrow_right_inner': (0,0), #eyebrow_GUOHUAA0090:1
    'eyebrow_right_outer': (0,1), #eyebrow_GUOHUAA0090:2
    'eyebrow_left_inner': (0,2),  #eyebrow_GUOHUAA0090:3
    'eyebrow_left_outer': (0,3),  #eyebrow_GUOHUAA0090:4
    'cheek_left_tendon': (2,0), #cheek_tendon_GUOHUAA0090:5
    'nose_left_tendon': (2,1), #cheek_tendon_GUOHUAA0090:6
    'nose_right_tendon': (2,2), #cheek_tendon_GUOHUAA0090:7
    'cheek_right_tendon': (2,3), #cheek_tendon_GUOHUAA0090:8

    #eye_rigid
    'eyeball_horizontal': (0,4), #connected to eye_m_shaped_board: 1
    'upper_eyelid_left': (0,5), 
    'lower_eyelid_left': (0,6),
    'upper_eyelid_right': (0,7),
    'lower_eyelid_right': (0,8),
    'eyeball_vertical': (0,9),
    
    #mouth_rigid
    'upper_lip_left': (1,0), #mouth_MG90S: 1
    'upper_lip_mid': (1,1), #mouth_MG90S: 11
    'upper_lip_right': (1,2), #mouth_MG90S: 10
    'mouth_right_corner_upper': (1,3), #mouth_MG90S: 8
    'mouth_right_corner_lower': (1,4), #mouth_MG90S: 9
    'mouth_left_corner_upper': (1,5), #mouth_MG90S: 6
    'mouth_left_corner_lower': (1,6), #mouth_MG90S: 7
    'lower_lip_left': (1,7), #mouth_MG90S: 18
    'lower_lip_right': (1,8), #mouth_MG90S: 17
    'lower_lip_mid_tendon': (1,9), #mouth_MG90S: 23
    'jaw_horizontal': (1,10), #mouth_MG90S: 16
    'jaw_right_upper':(1,11), #KS3518: 1
    'jaw_right_lower':(1,12), #mouth_MG90S: 2
    'jaw_left_upper':(1,13), #mouth_GUOHUAA0090: 1
    'tongue_upper':(1,14), #mouth_MG90S: 12
    'tongue_lower':(1,15), #mouth_MG90S: 21

    #neck_rigid
    'neck_left':(2,4), #neck_KS3518: 1
    'neck_right':(2,5), #neck_KS3518: 2
    
    

}