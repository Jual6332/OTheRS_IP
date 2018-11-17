// control_analysis/arduino-code/pidcontrol.cpp
// A simple PID controller implementation
// CPP FILE - Class implementation

#include "pidcontroller.h"
#include <Arduino.h>

PIDController::PIDController(float target, float Kp, float Kd, float Ki) {
    _Kp = Kp; // I know initializer lists are a feature of modern C++
    _Kd = Kd; // but I hate them.
    _Ki = Ki; 
    _target = target;

    // derivative control state variables
    _last_reading           = 0.0;
    _derivative_last_millis = 0;
    // integral control state variables
    _accumulated_err      = 0.0;
    _integral_last_millis = 0;
}

float PIDController::control(float reading) {
    unsigned long now = millis();
    return proportionalControl(reading) 
         + derivativeControl(reading, now) 
         + integralControl(reading, now);
}

// proportional control method
float PIDController::proportionalControl(float reading) {
    return _Kp * (_target - reading);
}

// derivative control method
float PIDController::derivativeControl(float reading) {
    unsigned long now = millis();
    return derivativeControl(reading, now);
}

// integral control method
float PIDController::integralControl(float reading) {
    unsigned long now = millis();
    return integralControl(reading, now);
}

/* PRIVATE */

// a method which accepts a particular timestamp is available for better precision
float PIDController::derivativeControl(float reading, unsigned long now) {

    // if this is the first time it's been called we can't calculate the 
    // derivative since there's no previous reading
    if (_derivative_last_millis == 0) {
        _derivative_last_millis = now;
        return 0.0;
    }

    // calculate the derivative using this measurement and the last
    float dt         = (float) (now - _derivative_last_millis) / 1000.0; // convert to seconds
    float delta      = reading - _last_reading;
    float derivative = delta / dt;

    _derivative_last_millis = now;

    return _Kd * derivative;
}

// a method which accepts a particular timestamp is available for better precision
float PIDController::integralControl(float reading, unsigned long now) {
    // sum error over all time
    float dt = now - _integral_last_millis;
    float err = _target - reading;

    _accumulated_err += err*dt;
    _integral_last_millis = now;

    return _Ki * _accumulated_err;
}
