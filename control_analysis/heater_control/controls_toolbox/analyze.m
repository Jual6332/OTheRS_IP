% TODO: find correct gains for everything
clear all; clc;

% Physical properties
m = 0.013; % kg
cp = 920;  % J / (kg * K)
kq = 0.1;  % heat loss (linearized)

plant = tf([0  1], ...
           [1, kq/(m*cp)])

% Control gains
kp = 100;
ki = 1e-2;
kd = -1e-2;

% Closed loop transfer function
closed_loop = tf([kd,         kp, ki], ...
                 [m*cp+kd, kq+kp, ki])

% simulate a step input
step(closed_loop)
