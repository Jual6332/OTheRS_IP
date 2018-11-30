% Modeled as a voltage - resistor network
% Qdot = current, T = voltage
% Qdot_vec = R_matrix * Voltage_vec
% 
clear all; clc; close all; format shortg;

Rc = 0.05;
Rl = 0.2;
Rg = 0.01;

R = [-(Rg + 2*Rc + Rl) Rc               Rc              Rl          Rg;
       Rc             -(Rg + 2*Rc + Rl) Rc              Rl          Rg;
       Rc              Rc             -(Rg + 2*Rc + Rl) Rl          Rg;
       Rl              Rl               Rl             -(3*Rl + Rg) Rg;
       0               0                0               0           0 ]

% initial temperatures
% TODO: Convert to initial thermal energies (Q = m*cp*T)
T_0 = [60   % Heater 1
       60   % Heater 2
       60   % Heater 2
       99   % Lepton
       25]; % Ground temp


[t, y] = ode45(@(t, T) R*T, [0, 60], T_0)


figure; hold on; grid on;
for i = 1:length(T_0)
    plot(t, y(:, i))
end
