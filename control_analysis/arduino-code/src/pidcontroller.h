// control_analysis/arduino-code/pidcontrol.cpp
// A simple PID controller implementation
// HEADER - Class definition

#pragma once

class PIDController {
public:
    // constructor
    PIDController(float target, float Kp, float Ki, float Kd);

    // run the control algorithm
    float control(float reading);

    // proportional control method
    float proportionalControl(float reading);

    // derivative control method
    float derivativeControl(float reading);

    // integral control method
    float integralControl(float reading);

private:
    // a method which accepts a particular timestamp is available for better precision
    float derivativeControl(float reading, unsigned long now);

    // a method which accepts a particular timestamp is available for better precision
    float integralControl(float reading, unsigned long now);

    // target temperature
    float _target;

    // Gains
    float _Kp;
    float _Kd;
    float _Ki;

    // state variables for derivative control
    float _last_reading;
    unsigned long _derivative_last_millis;

    // state variables for integral control
    float _accumulated_err;
    unsigned long _integral_last_millis;
};


