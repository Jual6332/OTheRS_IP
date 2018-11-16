/* control_analysis/arduino-code/src/main.ino - Jacob Killelea
 * Control Loop code to regulate heaters using an arduino
 */

// Heater physical properties
const float m  = 0.013; // Kg
const float cp = 920.0; // J/(Kg K)

// Thermistor physical properties
const float R25 = 0.0;    // Ohms
const float T25 = 25.0;   // deg C
const float R1  = 10.0e4; // Other resistor in the volage divider, ohms

// Control gains
const float Kp = 0.0; // Proportional
const float Ki = 0.0; // Integral
const float Kd = 0.0; // Derivative

// Control state variables - Heater 1
float therm1_last_reading       = 0.0; // Derivative control
unsigned long therm1_last_milis = 0;   // Derivative control
float therm1_err                = 0.0; // Integral control

// Control state variables - Heater 2
float therm2_last_reading       = 0.0; // Derivative control
unsigned long therm2_last_milis = 0;   // Derivative control
float therm2_err                = 0.0; // Integral control

#define THERMISTOR_1 A0
#define THERMISTOR_2 A1

#define HEATER_1 D9
#define HEATER_2 D11

void setup() {
    Serial.begin(9600);

    pinMode(THERMISTOR_1, INPUT);
    pinMode(THERMISTOR_2, INPUT);
    pinMode(HEATER_1,     OUTPUT);
    pinMode(HEATER_2,     OUTPUT);
}

void loop() {
}

float thermistor_read_degC(int thermistor_pin) {
    uint16_t adc = analogRead(thermistor_pin);
}

