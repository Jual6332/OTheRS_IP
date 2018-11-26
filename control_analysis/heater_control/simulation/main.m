% Compare the response of a linearized and nonlinear model for a simple resistive heater
% Jacob Killelea
% TODO: many of the coefficients in here are just guesses.
clear all;
close all;
% clc;

global integral_err;
global time_last;

% constants
TIME_SECONDS = 1;
TIME_MINUTES = 60*TIME_SECONDS;
TIME_HOURS   = 60*TIME_MINUTES;
sigma        = 1.380649e-23; % J * K^−1 boltzmann constant

Ttgt  = 100 + 273; % 100 degC
Tsurr = 20  + 273; % 20  degC, presumed to be the ambient temperature
T0    = Tsurr;      % Inital temperature of the heaters
                   % This is also the temperature about which the linearized model is
                   % actually linearized

m  = 13e-3; % kg
cp = 920;   % j / kg*K  MIL-HDBK-5J, Figure 3.2.1.0 Aluminum 2014-T6
Kc = 0.01;  % W / K
Kr = 0.001; % W / K^3 (check units?)

time_max = 2*TIME_HOURS; % seconds

Kp = Kc + 4*Kr*sigma*T0^3; % Proportional gain (calculated from delU = Ku*delT/[m*cp] -> such that delTdot = 0)
Kd = -1.0;                  % Integral gain
Ki = 5e-5;                 % Derivative gain

figure; hold on; grid on;

%%% Nonlinear simulation %%%
% Control law works on absoulte values
nonlinear_control_fn = @(T, t) control(T, t, Ttgt, Kp, Kd, Ki);

% Starts at an absoulte temperature
y0 = T0;

% Call ode45
[t_full, y_full] = ode45(@(t, y) nonlinear_odefn(t,                     ... 
                                                 y,                     ...
                                                 m,                     ... % Mass
                                                 cp,                    ... % Specific Heat
                                                 Tsurr,                 ... % Surrounding temperature
                                                 Kc,                    ... % Conduction + Convection coeff
                                                 Kr,                    ... % Radiation coeff
                                                 nonlinear_control_fn), ... % Control Function
                                             [0, time_max],             ... % Time range
                                             y0);                           % Initial state (just T0)

plot(t_full/TIME_HOURS, y_full - 273, 'b',            ...
                                      'linewidth', 2, ...
                                      'displayname', 'Nonlinear Model')

%%% Linearized Model %%%
% The control law drives the temperature to an offset (Ttgt - T0) instead of an absolute value (Ttgt)

% Reset stateful variables from control algorithm
integral_err = 0;
time_last = 0;

linear_control_fn = @(T, t) control(T, t, Ttgt - T0, Kp, Kd, Ki); % drive to an offset from T0

% For the linearized model, it starts at an offset from T0, not an absolute temperature
y0 = 0;

% Call ode45
[t_lin, y_lin] = ode45(@(t, y) linear_odefn(t,                  ...
                                            y,                  ...
                                            m,                  ...
                                            cp,                 ...
                                            T0,                 ...
                                            Kc,                 ...
                                            Kr,                 ...
                                            linear_control_fn), ...
                                        [0, time_max],          ...
                                        y0);                        % Starts at offset from T0
y_lin = y_lin + T0; % add the simulated changes to the zero point

plot(t_lin/TIME_HOURS,  y_lin - 273, 'r',            ...
                                     'linewidth', 2, ...
                                     'displayname', 'Linearized Model')

% Target and ambient temperatures
plot([0, time_max/TIME_HOURS], [Ttgt,  Ttgt]  - 273, 'r', ...
                            'displayname', 'Target Temperature')
plot([0, time_max/TIME_HOURS], [Tsurr, Tsurr] - 273, 'b', ...
                            'displayname', 'Ambient Temperature')

title(sprintf('Temperature over time (K_P=%.1d, K_I=%.1d, K_D=%.1d)', Kp, Ki, Kd))
xlabel('Time (hours)')
ylabel('Temperature (deg C)')
legend('show', 'location', 'southeast')
ylim([0, 120])

fprintf('Linearized max overshoot %f\n', max(y_lin - Ttgt));
