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

Mr = 2e-3; % resistor = 2g
Mlept = 100e-3; % Lepton = 100g including pcb(?)
cp_r = 200; % J/kg*K
cp_lept = 400; % J/kg*K

M_cp = [Mr*cp_r
       Mr*cp_r
       Mr*cp_r
       Mlept*cp_lept
       1]; 
T_0 = [60   % Heater 1
       60   % Heater 2
       60   % Heater 2
       99   % Lepton
       25]; % Ground temp
T_0 = T_0 + 273; % Kelvin

Q_0 = M_cp .* T_0

[t, Q] = ode45(@(t, T) R*T, [0, 60], Q_0)

% Divide resulting energies my M*cp
T = Q ./ repmat(M_cp', length(Q), 1) - 273

figure; hold on; grid on;
for i = 1:length(Q_0)
    plot(t, T(:, i))
end
