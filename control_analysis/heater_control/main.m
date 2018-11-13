% Compare the response of a linearized and nonlinear model for a simple resistive heater
% Jacob Killelea
% TODO: many of the coefficients in here are just guesses.
clear all; clc; close all;

% constants
TIME_SECONDS = 1;
TIME_MINUTES = 60*TIME_SECONDS;
TIME_HOURS   = 60*TIME_MINUTES;
sigma        = 1.380649e-23; % J * K^−1 boltzmann constant

Ttgt  = 100 + 273; % 100 degC
Tsurr = 20  + 273; % 20  degC, presumed to be the ambient temperature
T0    = Ttgt;      % Inital temperature of the heaters
                   % This is also the temperature about which the linearized model is
                   % actually linearized

m  = 13e-3; % kg
cp = 920;   % j / kg*K  MIL-HDBK-5J, Figure 3.2.1.0 Aluminum 2014-T6
Kc = 0.01;  % W / K
Kr = 0.001; % W / K^3 (check units?)

time_max = 2*TIME_HOURS; % seconds

Kp = Kc + 4*Kr*sigma*T0^3 % proportional gain (calculated from delU = Ku*delT/[m*cp] -> such that delTdot = 0)
Kd = 0;                   % unimplemented
Ki = 0.001;               % implemented in a very bad way

figure; hold on; grid on;

%%% Nonlinear simulation %%%
% Control law works on absoulte values
nonlinear_control_fn = @(T, t) control(T, t, Ttgt, Kp, Kd, Ki);

% Starts at an absoulte temperature
y0 = T0;

% Call ode45
[t_full, y_full] = ode45(@(t, y) nonlinear_odefn(t, y, m, cp, Tsurr, Kc, Kr, nonlinear_control_fn), [0, time_max], y0);

plot(t_full/TIME_HOURS, y_full - 273, 'b',            ...
                                      'linewidth', 2, ...
                                      'displayname', 'Nonlinear Model')

%%% Linearized Model %%%
% The control law drives the temperature to an offset (Ttgt - T0) instead of an absolute value (Ttgt)
linear_control_fn = @(T, t) control(T, t, (Ttgt - T0), Kp, Kd, Ki);

% For the linearized model, it starts at an offset from T0, not an absolute temperature
y0 = 0;

% Call ode45
[t_lin, y_lin] = ode45(@(t, y) linear_odefn(t, y, m, cp, T0, Kc, Kr, linear_control_fn), [0, time_max], y0);
y_lin = y_lin + T0; % add the simulated changes to the zero point

plot(t_lin/TIME_HOURS,  y_lin - 273, 'r',            ...
                                     'linewidth', 2, ...
                                     'displayname', 'Linearized Model')

% Target and ambient temperatures
plot([0, time_max/TIME_HOURS], [Ttgt,  Ttgt]  - 273, 'r', ...
                            'displayname', 'Target Temperature')
plot([0, time_max/TIME_HOURS], [Tsurr, Tsurr] - 273, 'b', ...
                            'displayname', 'Ambient Temperature')

title(sprintf('Temperature over time (K_p = %f, K_I = %f)', Kp, Ki))
xlabel('Time (hours)')
ylabel('Temperature (deg C)')
legend('show', 'location', 'southeast')
ylim([0, 120])
