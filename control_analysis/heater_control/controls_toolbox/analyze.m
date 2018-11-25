% TODO: find correct gains for everything
clear all; close all; clc;

% Physical properties
m = 0.013; % kg
cp = 920;  % J / (kg * K)
kq = 0.1;  % heat loss (linearized)

% open loop
plant = tf([0  1], ...
           [1, kq/(m*cp)]);

% Control gains
kp = 1;
ki = 5e-3;
kd = -1e-2;

% Closed loop transfer function
closed_loop = tf([kd,         kp, ki], ...
                 [m*cp+kd, kq+kp, ki])

% simulate a step input
step(closed_loop)
