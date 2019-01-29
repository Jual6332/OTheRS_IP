/* control_analysis/arduino-code/src/main.ino - Jacob Killelea
 * Control Loop code to regulate heaters using an arduino
 *
 */

#include "pidcontroller.h"

// Heater physical properties
const float m  = 0.013; // Kg
const float R  = 10; // Ohm
const float cp = 920.0; // J/(Kg K)
const float Kc = 0.01;  // Conduction
const float Kr = 0.001; // Radiation
const float T0 = 373;   // Linearize about 100 degC
const float sigma = 1.3809649e-23; // Boltzman constant

// Thermistor reference properties
const float R25 = 0.0;    // Ohms
const float T25 = 25.0;   // deg C
const float R1  = 10.0e4; // Other resistor in the volage divider, ohms

// Control variables
const float target = 100.0; // target temperature
const float Kp = Kc + 4*Kr*sigma*pow(T0, 3); // Proportional gain
const float Ki = 5e-5; // Integral gain
const float Kd = 0.0; // Derivative gain

#define THERMISTOR_1 A0
#define THERMISTOR_2 A1

#define HEATER_1 9
#define HEATER_2 11

PIDController heater1(target, Kp, Ki, Kd);
PIDController heater2(target, Kp, Ki, Kd);

void setup() {
    Serial.begin(9600);

    pinMode(THERMISTOR_1, INPUT);
    pinMode(THERMISTOR_2, INPUT);
    pinMode(HEATER_1,     OUTPUT);
    pinMode(HEATER_2,     OUTPUT);
}

void loop() {
    float qin = heater1.control(thermistor_read_degC(THERMISTOR_1));
}

float thermistor_read_degC(int thermistor_pin) {
    uint16_t adc = analogRead(thermistor_pin);
    return 0.0; // TODO
}

