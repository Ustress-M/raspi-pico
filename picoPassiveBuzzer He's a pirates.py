'''
2023.05.30
writer : minsu bak
mail : m.bak@outlook.kr
'''

import machine
import utime

songspeed = 1.1

NOTE_C4 = 262
NOTE_D4 = 294
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_G4 = 392
NOTE_A4 = 440
NOTE_B4 = 494
NOTE_C5 = 523
NOTE_D5 = 587
NOTE_E5 = 659
NOTE_F5 = 698
NOTE_G5 = 784
NOTE_A5 = 880
NOTE_B5 = 988


notes = [
    NOTE_E4, NOTE_G4, NOTE_A4, NOTE_A4, 8,
    NOTE_A4, NOTE_B4, NOTE_C5, NOTE_C5, 8,
    NOTE_C5, NOTE_D5, NOTE_B4, NOTE_B4, 8,
    NOTE_A4, NOTE_G4, NOTE_A4, 8,

    NOTE_E4, NOTE_G4, NOTE_A4, NOTE_A4, 8,
    NOTE_A4, NOTE_B4, NOTE_C5, NOTE_C5, 8,
    NOTE_C5, NOTE_D5, NOTE_B4, NOTE_B4, 8,
    NOTE_A4, NOTE_G4, NOTE_A4, 8,

    NOTE_E4, NOTE_G4, NOTE_A4, NOTE_A4, 8,
    NOTE_A4, NOTE_C5, NOTE_D5, NOTE_D5, 8,
    NOTE_D5, NOTE_E5, NOTE_F5, NOTE_F5, 8,
    NOTE_E5, NOTE_D5, NOTE_E5, NOTE_A4, 8,

    NOTE_A4, NOTE_B4, NOTE_C5, NOTE_C5, 8,
    NOTE_D5, NOTE_E5, NOTE_A4, 8,
    NOTE_A4, NOTE_C5, NOTE_B4, NOTE_B4, 8,
    NOTE_C5, NOTE_A4, NOTE_B4, 8,

    NOTE_A4, NOTE_A4,
    # Repeat of first part
    NOTE_A4, NOTE_B4, NOTE_C5, NOTE_C5, 8,
    NOTE_C5, NOTE_D5, NOTE_B4, NOTE_B4, 8,
    NOTE_A4, NOTE_G4, NOTE_A4, 8,

    NOTE_E4, NOTE_G4, NOTE_A4, NOTE_A4, 8,
    NOTE_A4, NOTE_B4, NOTE_C5, NOTE_C5, 8,
    NOTE_C5, NOTE_D5, NOTE_B4, NOTE_B4, 8,
    NOTE_A4, NOTE_G4, NOTE_A4, 8,

    NOTE_E4, NOTE_G4, NOTE_A4, NOTE_A4, 8,
    NOTE_A4, NOTE_C5, NOTE_D5, NOTE_D5, 8,
    NOTE_D5, NOTE_E5, NOTE_F5, NOTE_F5, 8,
    NOTE_E5, NOTE_D5, NOTE_E5, NOTE_A4, 8,

    NOTE_A4, NOTE_B4, NOTE_C5, NOTE_C5, 8,
    NOTE_D5, NOTE_E5, NOTE_A4, 8,
    NOTE_A4, NOTE_C5, NOTE_B4, NOTE_B4, 8,
    NOTE_C5, NOTE_A4, NOTE_B4, 8,
    # End of Repeat

    NOTE_E5, 8, 8, NOTE_F5, 8, 8,
    NOTE_E5, NOTE_E5, 8, NOTE_G5, 8, NOTE_E5, NOTE_D5, 8, 8,
    NOTE_D5, 8, 8, NOTE_C5, 8, 8,
    NOTE_B4, NOTE_C5, 8, NOTE_B4, 8, NOTE_A4,

    NOTE_E5, 8, 8, NOTE_F5, 8, 8,
    NOTE_E5, NOTE_E5, 8, NOTE_G5, 8, NOTE_E5, NOTE_D5, 8, 8,
    NOTE_D5, 8, 8, NOTE_C5, 8, 8,
    NOTE_B4, NOTE_C5, 8, NOTE_B4, 8, NOTE_A4
]

duration = [
    125, 125, 250, 125, 125,
    125, 125, 250, 125, 125,
    125, 125, 250, 125, 125,
    125, 125, 375, 125,

    125, 125, 250, 125, 125,
    125, 125, 250, 125, 125,
    125, 125, 250, 125, 125,
    125, 125, 375, 125,

    125, 125, 250, 125, 125,
    125, 125, 250, 125, 125,
    125, 125, 250, 125, 125,
    125, 125, 125, 250, 125,

    125, 125, 250, 125, 125,
    250, 125, 250, 125,
    125, 125, 250, 125, 125,
    125, 125, 375, 375,

    250, 125,
    125, 125, 250, 125, 125,
    125, 125, 250, 125, 125,
    125, 125, 375, 125,

    125, 125, 250, 125, 125,
    125, 125, 250, 125, 125,
    125, 125, 250, 125, 125,
    125, 125, 375, 125,

    125, 125, 250, 125, 125,
    125, 125, 250, 125, 125,
    125, 125, 250, 125, 125,
    125, 125, 125, 250, 125,

    125, 125, 250, 125, 125,
    250, 125, 250, 125,
    125, 125, 250, 125, 125,
    125, 125, 375, 375,

    250, 125, 375, 250, 125, 375,
    125, 125, 125, 125, 125, 125, 125, 125, 375,
    250, 125, 375, 250, 125, 375,
    125, 125, 125, 125, 125, 500,

    250, 125, 375, 250, 125, 375,
    125, 125, 125, 125, 125, 125, 125, 125, 375,
    250, 125, 375, 250, 125, 375,
    125, 125, 125, 125, 125, 500
]

# Set up the Pico
import machine
pwm = machine.PWM(machine.Pin(15))
pwm.freq(440)
pwm.duty_u16(65535//2)

# Play the melody
for i in range(len(notes)):
    
    wait = int(duration[i] * songspeed) *0.001
    
    if  notes[i] == 8:
        pwm.duty_u16(0)
    elif notes[i] != 8:
        pwm.duty_u16(65535//4)
    print(f'note 값은 : {notes[i]}')
    pwm.freq(notes[i])
    
    print(f'wait의 값은 : {wait}')
    utime.sleep(wait)

pwm.freq(440)
pwm.duty_u16(0)





