# Mapping Logic
# This module defines the mapping between parts, PWM boards and their corresponding GPIO pins.

# Board 1 (0x40): connecting to parts eye and eyebrow
# Board 2 (0x41): connecting to part mouth
# Board 3 (0x42): connecting to part neck and tendon-driven servos

# Pattern: 'function_name': (board_address, pin_number)
# Board ID: 0=0x41, 1=0x40, 2=0x42

MOTOR_MAP = {
    #eyebrow_rigid
    0: (0,0), #eyebrow_GUOHUAA0090:1 'eyebrow_right_inner'
    1: (0,1), #eyebrow_GUOHUAA0090:2 'eyebrow_right_outer'
    2: (0,2),  #eyebrow_GUOHUAA0090:3 'eyebrow_left_inner'
    3: (0,3),  #eyebrow_GUOHUAA0090:4 'eyebrow_left_outer'
    4: (2,0), #cheek_tendon_GUOHUAA0090:5 'cheek_left_tendon'
    5: (2,1), #cheek_tendon_GUOHUAA0090:6 'nose_left_tendon'
    6: (2,2), #cheek_tendon_GUOHUAA0090:7 'nose_right_tendon'
    7: (2,3), #cheek_tendon_GUOHUAA0090:8 'cheek_right_tendon'

    #eye_rigid
    8: (0,4), #connected to eye_m_shaped_board: 1
    9: (0,5), 
    10: (0,6),
    11: (0,7),
    12: (0,8),
    13: (0,9),
    
    #mouth_rigid
    14: (1,0), #mouth_MG90S: 1 'upper_lip_left'
    15: (1,1), #mouth_MG90S: 11 'upper_lip_mid'
    16: (1,2), #mouth_MG90S: 10 'upper_lip_right'
    17: (1,3), #mouth_MG90S: 8 'mouth_right_corner_upper'
    18: (1,4), #mouth_MG90S: 9 'mouth_right_corner_lower'
    19: (1,5), #mouth_MG90S: 6 'mouth_left_corner_upper'
    20: (1,6), #mouth_MG90S: 7 'mouth_left_corner_lower'
    21: (1,7), #mouth_MG90S: 18 'lower_lip_left'
    22: (1,8), #mouth_MG90S: 17 'lower_lip_right'
    23: (1,9), #mouth_MG90S: 23 'lower_lip_mid_tendon'
    24: (1,10), #mouth_MG90S: 16 'jaw_horizontal'
    25: (1,11), #KS3518: 1 'jaw_right_upper'
    26: (1,12), #mouth_MG90S: 2 'jaw_right_lower'
    27: (1,13), #mouth_GUOHUAA0090: 1 'jaw_left_upper'
    28: (1,14), #mouth_MG90S: 12 'tongue_upper'
    29: (1,15), #mouth_MG90S: 21 'tongue_lower'

    #neck_rigid
    30: (2,4), #neck_KS3518: 1 'neck_left'
    31: (2,5), #neck_KS3518: 2 'neck_right'
    
    

}